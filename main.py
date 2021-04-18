import random
import pygame

import Bonuses
from CBoard import Board
from CBoard import board_gen
import Pieces

pygame.init()
title_font = pygame.font.SysFont("Comic Sans MS", 96)
title_desc_font = pygame.font.SysFont("Comic Sans MS", 48)
upgrade_type_font = title_desc_font
upgrade_desc_font = pygame.font.SysFont("Comic Sans MS", 36)

title_screen = pygame.display.set_mode((800, 800))
white_diagonal_upgrades = []
white_horizontal_upgrades = []
white_knighted_upgrades = []
black_diagonal_upgrades = []
black_horizontal_upgrades = []
black_knighted_upgrades = []
board: Board.Board = None
kings = {}
show_welcome = True
show_rules = False
end = False
game_over = False
two_player = False


def welcome_screen():
    title_screen.fill((0, 0, 0))
    title = title_font.render("Weird Chess", True, (255, 255, 255))
    title_desc = title_desc_font.render("Press space to play, or press \"r\" to see rules", True, (255, 255, 255))

    title_screen.blit(title, (800 // 2 - title.get_width() // 2, 200))
    title_screen.blit(title_desc, (800 // 2 - title_desc.get_width() // 2, 800 // 2 - title_desc.get_height() // 2))


def rules_screen():
    title_screen.fill((0, 0, 0))
    rule_objs = []
    rules = ["1. Pieces move like they do in normal chess.",
             "2. However, check and checkmate doesn't apply.",
             "3. The goal is the capture the opponent's king.",
             "4. At the end of the game, the winner will get ",
             "  to choose an upgrade type.",
             "        4a. This upgrade type will be applied to one of",
             "          the winner's piece types at random,",
             "          based on the upgrade.",
             "5. The more games you play, the bigger the board gets.",
             "",
             "Press ESC to return to the welcome screen."]

    for rule in rules:
        rule_objs.append(upgrade_desc_font.render(rule, True, (255, 255, 255)))
    rules_title = upgrade_type_font.render("Rules:", True, (255, 255, 255))

    title_screen.blit(rules_title, (0, 0))
    offset = rules_title.get_height() + 10
    for rule in rule_objs:
        title_screen.blit(rule, (0, offset))
        offset += rule.get_height() + 10


def init_board(size):
    global wins, board, screen, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades, black_diagonal_upgrades, black_horizontal_upgrades, black_knighted_upgrades, kings, end, game_over, you_lose, you_win, turn
    print(white_diagonal_upgrades)
    print(white_horizontal_upgrades)
    print(white_knighted_upgrades)
    print(black_diagonal_upgrades)
    print(black_horizontal_upgrades)
    print(black_knighted_upgrades)
    end = False
    game_over = False
    you_lose = False
    you_win = False
    turn = True
    size = 2 * size + 6
    board = Board.Board(size)
    screen = board.create_board()
    kings = board_gen.gen_board(board, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades,
                                black_diagonal_upgrades, black_horizontal_upgrades, black_knighted_upgrades)


level = 1

youwin_image = upgrade_type_font.render("you win", True, (0, 255, 0))
youlose_image = upgrade_type_font.render("you lose", True, (255, 0, 0))

selected: Pieces.Piece = None
turn = True  # True = white, False = black


def upgrade(color: bool, choice: int):
    global level, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades, black_diagonal_upgrades,\
        black_horizontal_upgrades, black_knighted_upgrades, game_over
    wupgrades = [random.choice(list(set(Bonuses.Diagonal.get_pieces()) - set(white_diagonal_upgrades))),
                 random.choice(list(set(Bonuses.Horizontal.get_pieces()) - set(white_horizontal_upgrades))),
                 random.choice(list(set(Bonuses.Knighted.get_pieces()) - set(white_knighted_upgrades)))]

    bupgrades = [random.choice(list(set(Bonuses.Diagonal.get_pieces()) - set(black_diagonal_upgrades))),
                 random.choice(list(set(Bonuses.Horizontal.get_pieces()) - set(black_horizontal_upgrades))),
                 random.choice(list(set(Bonuses.Knighted.get_pieces()) - set(black_knighted_upgrades)))]

    if color:
        if choice == 1:
            white_diagonal_upgrades.append(wupgrades[0])
        elif choice == 2:
            white_horizontal_upgrades.append(wupgrades[1])
        elif choice == 3:
            white_knighted_upgrades.append(wupgrades[2])
    else:
        if choice == 1:
            black_diagonal_upgrades.append(bupgrades[0])
        elif choice == 2:
            black_horizontal_upgrades.append(bupgrades[1])
        elif choice == 3:
            black_knighted_upgrades.append(bupgrades[2])
    game_over = False
    level += 1
    init_board(level)


while not end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            end = True

        if show_welcome:
            welcome_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_welcome = False
                    init_board(level)
                if event.key == pygame.K_r:
                    show_rules = True
                    show_welcome = False

        elif show_rules:
            rules_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_rules = False
                    show_welcome = True

        elif not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not two_player and not turn:
                    pass
                else:
                    square = board.get_square((pygame.mouse.get_pos()[0] // 80, pygame.mouse.get_pos()[1] // 80))

                    if selected is None:
                        if square.has_piece and square.piece.color == turn:
                            selected = square.piece
                            if not selected.moves:
                                selected = None
                    else:
                        if selected == square.piece:
                            selected = None
                        elif any(square == board.get_square(i) for i in selected.moves):
                            selected.move(square.board_pos)
                            selected = None
                            turn = not turn
                        elif square.piece is None:
                            selected = None
                        elif square.piece.color == selected.color:
                            selected = square.piece

                    if square.piece is not None:
                        if selected and square.piece != selected:
                            if any(square == board.get_square(i) for i in selected.moves):
                                selected.capture(square.piece)
                            else:
                                if square.piece == turn:
                                    selected = square.piece

            if not two_player and not turn:
                rand_piece = random.choice([i for i in board.black_pieces])
                while not rand_piece.moves:
                    rand_piece = random.choice([i for i in board.black_pieces])

                rand_piece.move(random.choice(rand_piece.moves))
                turn = True

            for i in board.board:
                for k in i:
                    pygame.draw.rect(screen, k.color, k.rect)

            for i in board.white_pieces:
                i.update_piece()
            for i in board.black_pieces:
                i.update_piece()

            if not kings["white"].alive():
                game_over = True
                wins = False

            if not kings["black"].alive():
                game_over = True
                wins = True

            board.white_pieces.draw(screen)
            board.black_pieces.draw(screen)

            if selected is not None:
                selected.on_select()

        if game_over:
            screen.fill((0, 0, 0))

            diag_title = upgrade_type_font.render(Bonuses.Diagonal.get_name()[0], True, (255, 0, 0))
            diag_body = upgrade_desc_font.render(Bonuses.Diagonal.get_name()[1], True, (255, 0, 0))

            horiz_title = upgrade_type_font.render(Bonuses.Horizontal.get_name()[0], True, (255, 255, 0))
            horiz_body = upgrade_desc_font.render(Bonuses.Horizontal.get_name()[1], True, (255, 255, 0))

            knighted_title = upgrade_type_font.render(Bonuses.Knighted.get_name()[0], True, (0, 255, 0))
            knighted_body = upgrade_desc_font.render(Bonuses.Knighted.get_name()[1], True, (0, 255, 0))

            screen.blit(diag_title, (0, 0))
            screen.blit(diag_body, (0, diag_title.get_height()))

            screen.blit(horiz_title,
                        (0, screen.get_height() // 2 - horiz_title.get_height() // 2 - horiz_body.get_height()))
            screen.blit(horiz_body, (0, screen.get_height() // 2))

            screen.blit(knighted_title,
                        (0, screen.get_height() - knighted_title.get_height() - knighted_body.get_height()))
            screen.blit(knighted_body, (0, screen.get_height() - knighted_body.get_height()))

            pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if two_player:
                        upgrade(wins, 1)
                    elif wins:
                        upgrade(wins, 1)
                        upgrade(False, 1)
                if event.key == pygame.K_2:
                    if two_player:
                        upgrade(wins, 2)
                    elif wins:
                        upgrade(wins, 2)
                        upgrade(False, 2)
                if event.key == pygame.K_3:
                    if two_player:
                        upgrade(wins, 3)
                    elif wins:
                        upgrade(wins, 3)
                        upgrade(False, 3)

        pygame.display.flip()

pygame.quit()

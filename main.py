import random
import pygame

import Bonuses
from CBoard import Board
from CBoard import board_gen
import Pieces

pygame.init()

white_diagonal_upgrades = []
white_horizontal_upgrades = []
white_knighted_upgrades = []
black_diagonal_upgrades = []
black_horizontal_upgrades = []
black_knighted_upgrades = []
screen = None
board = None
kings = {}


def init_board(size):

    global wins, board, screen, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades, black_diagonal_upgrades, black_horizontal_upgrades, black_knighted_upgrades, kings, gameEnd, game_over, you_lose, you_win, turn
    print(white_diagonal_upgrades)
    print(white_horizontal_upgrades)
    print(white_knighted_upgrades)
    print(black_diagonal_upgrades)
    print(black_horizontal_upgrades)
    print(black_knighted_upgrades)
    gameEnd = False
    game_over = False
    you_lose = False
    you_win = False
    turn = True
    size = 2 * size + 6
    board = Board.Board(size)
    screen = board.create_board()
    kings = board_gen.gen_board(board, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades, black_diagonal_upgrades, black_horizontal_upgrades, black_knighted_upgrades)


level = 4
font = pygame.font.SysFont("Comic Sans MS", 48)
font2 = pygame.font.SysFont("Comic Sans MS", 36)
youwin_image = font.render("you win", True, (0, 255, 0))
youlose_image = font.render("you lose", True, (255, 0, 0))

selected: Pieces.Piece = None
turn = True  # True = white, False = black


def upgrade(color: bool, choice: int):
    global level, white_diagonal_upgrades, white_horizontal_upgrades, white_knighted_upgrades, black_diagonal_upgrades, black_horizontal_upgrades, black_knighted_upgrades, game_over
    upgrades = [random.choice(Bonuses.Diagonal.get_pieces()),
                random.choice(Bonuses.Horizontal.get_pieces()), random.choice(Bonuses.Knighted.get_pieces())]

    if color:
        if choice == 1:
            white_diagonal_upgrades.append(upgrades[0])
        elif choice == 2:
            white_horizontal_upgrades.append(upgrades[1])
        elif choice == 3:
            white_knighted_upgrades.append(upgrades[2])
    else:
        if choice == 1:
            black_diagonal_upgrades.append(upgrades[0])
        elif choice == 2:
            black_horizontal_upgrades.append(upgrades[1])
        elif choice == 3:
            black_knighted_upgrades.append(upgrades[2])
    game_over = False
    level += 1
    init_board(level)


init_board(level)

while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
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

        for i in board.board:
            for k in i:
                pygame.draw.rect(screen, k.color, k.rect)

        board.white_pieces.draw(screen)

        board.black_pieces.draw(screen)

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

        if you_win:
            screen.blit(youwin_image, (screen.get_width() // 2 - youwin_image.get_width() // 2, screen.get_height() // 2 - youwin_image.get_height() // 2))

        if you_lose:
            screen.blit(youlose_image, (screen.get_width() // 2 - youlose_image.get_width() // 2, screen.get_height() // 2 - youlose_image.get_height() // 2))

        if game_over:
            screen.fill((0, 0, 0))

            diag_title = font.render(Bonuses.Diagonal.get_name()[0], True, (255, 0, 0))
            diag_body = font2.render(Bonuses.Diagonal.get_name()[1], True, (255, 0, 0))

            horiz_title = font.render(Bonuses.Horizontal.get_name()[0], True, (255, 255, 0))
            horiz_body = font2.render(Bonuses.Horizontal.get_name()[1], True, (255, 255, 0))

            knighted_title = font.render(Bonuses.Knighted.get_name()[0], True, (0, 255, 0))
            knighted_body = font2.render(Bonuses.Knighted.get_name()[1], True, (0, 255, 0))

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
                    upgrade(wins, 1)

                if event.key == pygame.K_2:
                    upgrade(wins, 2)

                if event.key == pygame.K_3:
                    upgrade(wins, 3)

        if selected is not None:
            selected.on_select()

        pygame.display.flip()

pygame.quit()

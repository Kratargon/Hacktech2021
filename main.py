import pygame

from CBoard import Board
from CBoard import board_gen
import Pieces
from Pieces import King



pygame.init()

board = Board.Board(8)
font = pygame.font.SysFont("Comic Sans MS", 48)
youwin_image = font.render("you win", True, (0, 255, 0))

youlose_image = font.render("you lose", True, (255, 0, 0))


screen = board.create_board()
board.screen = screen

board_gen.gen_board(board)

wking = Pieces.King(board, board.get_square((4, 7)), True)
board.white_pieces.add(wking)

bking = Pieces.King(board, board.get_square((3, 0)), False)
board.white_pieces.add(bking)

gameEnd = False
upgrade = False
game_over = False
you_lose = False
you_win = False
selected: Pieces.Piece = None
turn = True  # True = white, False = black

while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and not upgrade:
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

    if not wking.alive():
        game_over = True
        you_lose = True

    if not bking.alive():
        game_over = True
        you_win = True

    if you_win:
        screen.blit(youwin_image, (screen.get_width() // 2 - youwin_image.get_width() // 2, screen.get_height() // 2 - youwin_image.get_height() // 2))

    if you_lose:
        screen.blit(youlose_image, (screen.get_width() // 2 - youlose_image.get_width() // 2, screen.get_height() // 2 - youlose_image.get_height() // 2))

    if selected is not None:
        selected.on_select()

    pygame.display.flip()

pygame.quit()

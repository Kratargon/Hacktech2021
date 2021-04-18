import pygame

from CBoard import Board
from CBoard import board_gen
import Pieces

pygame.init()

board = Board.Board(8)

screen = board.create_board()
board.screen = screen

board_gen.gen_board(board)

gameEnd = False
selected: Pieces.Piece = None
turn = True  # True = white, False = black

while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
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

    if selected is not None:
        selected.on_select()

    # print(brook.can_capture_(wking.game_pos))
    pygame.display.flip()

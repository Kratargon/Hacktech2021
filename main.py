import pygame

from Board import Board
import Pieces

pygame.init()

board = Board.Board(8)
board.white_pieces = pygame.sprite.Group()
board.black_pieces = pygame.sprite.Group()

screen = board.create_board()
board.screen = screen
wking = Pieces.King(board, board.get_square((4, 7)), True)
brook = Pieces.Rook(board, board.get_square((1, 1)), False)
brook1 = Pieces.Rook(board, board.get_square((2, 2)), False)

wbishop = Pieces.Bishop(board, board.get_square((5, 5)), True)

board.white_pieces.add(wking, wbishop)
board.black_pieces.add(brook, brook1)
gameEnd = False
selected: Pieces.Piece = None

while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            square = board.get_square((pygame.mouse.get_pos()[0] // 80, pygame.mouse.get_pos()[1] // 80))

            if selected is None:
                selected = square.piece

            else:
                if selected == square.piece:
                    selected = None
                elif any(square == board.get_square(i) for i in selected.moves):
                    selected.move(square.board_pos)
                    selected = None

            if square.piece is not None:
                if selected and square.piece != selected:
                    if any(square == board.get_square(i) for i in selected.moves):
                        selected.capture(square.piece)
                    else:
                        selected = square.piece

            print(selected)

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

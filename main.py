import pygame

from Board import Board
import Pieces

pygame.init()

board = Board.Board(8)
board.white_pieces = pygame.sprite.Group()
board.black_pieces = pygame.sprite.Group()

screen = board.create_board()

wking = Pieces.King(board, board.get_square((4, 7)), True)
wrook = Pieces.Rook(board, board.get_square((1, 1)), True)
wbishop = Pieces.Bishop(board, board.get_square((5, 5)), True)

board.white_pieces.add(wking, wrook, wbishop)
gameEnd = False


while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            square = board.get_square((pygame.mouse.get_pos()[0] // 80, pygame.mouse.get_pos()[1] // 80))
            print((pygame.mouse.get_pos()[0] // 80, pygame.mouse.get_pos()[1] // 80))
            if square.piece is not None:
                print(square)
                square.piece.on_select()
            else:
                wpawn = Pieces.Pawn(board, square, True)
                board.white_pieces.add(wpawn)

    for i in board.board:
        for k in i:
            pygame.draw.rect(screen, k.color, k.rect)

    board.white_pieces.draw(screen)

    board.black_pieces.draw(screen)

    pygame.display.flip()

import pygame

from Board import Board
from Pieces.King import King

pygame.init()

board = Board.Board(8)
board.white_pieces = pygame.sprite.Group()
board.black_pieces = pygame.sprite.Group()

wking = King(board, board.get_square((0, 0)), True)

wking.add(board.white_pieces)
wking.image = pygame.image.load("textures/king.png")
wking.rect = wking.image.get_rect()
wking.rect.x = 0
wking.rect.y = 0

screen = board.create_board()

gameEnd = False


while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True

    for i in board.board_rects:
        pygame.draw.rect(screen, i.color, i.rect)

    board.white_pieces.draw(screen)
    board.black_pieces.draw(screen)

    pygame.display.flip()

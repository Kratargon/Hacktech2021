import pygame

from Board import Square


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[] for i in range(size)]
        for i in range(size):
            for k in range(size):
                self.board[i].append(Square.Square((i, k)))
        self.board_rects = []
        self.white_pieces = None
        self.black_pieces = None

    def create_board(self):
        temp = pygame.display.set_mode((self.size * self.size * 10, self.size * self.size * 10))

        flag = False
        current_coords = [0, 0]
        color = (80, 80, 80)
        size = self.size ** 2 * 10
        for i in range(self.size ** 2):
            if flag:
                self.board_rects.append(BoardRect(current_coords[0], current_coords[1], color))
            else:
                self.board_rects.append(BoardRect(current_coords[0], current_coords[1], (0, 0, 0)))
            current_coords[0] += self.size * 10
            if current_coords[0] >= size:
                current_coords[1] += self.size * 10
                current_coords[0] = 0
                flag = not flag
            if current_coords[1] >= size:
                current_coords[0] += self.size * 10
                current_coords[1] = 0
                flag = not flag
            flag = not flag

        return temp

    def get_square(self, pos: tuple) -> Square.Square:
        x = pos[1]
        y = pos[0]
        return self.board[x][y]

    def check_bounds(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size


class BoardRect(pygame.sprite.Sprite):
    def __init__(self, posx, posy, color):
        super().__init__()
        self.rect = pygame.Rect(posx, posy, 80, 80)
        self.position = posx, posy
        self.color = color

import operator, pygame

from Board import Board, Square
from Utils.utils import add


class Piece(pygame.sprite.Sprite):
    def __init__(self, board: Board.Board, square: Square.Square, color: bool):
        super().__init__()
        self.pos = square.pos
        self.board = board
        self.square = square
        self.piece_moves = []
        self.color = color  # True is white, False is black
        square.piece = self

    def can_capture(self, pos: tuple) -> bool:
        if self.can_move(pos) and self.board.get_square(pos).has_piece:
            if self.board.get_square(pos).piece.color is not self.color:
                return True

    def can_move(self, pos: tuple) -> bool:
        possible_locs = [add(self.pos, move) for move in self.piece_moves]
        if any(pos == i for i in possible_locs):
            if any(self.board.get_square(i).has_piece for i in possible_locs):
                return False
        return True

    def move(self, pos: tuple):
        self.pos = tuple(map(operator.add, self.pos, pos))
        self.square.has_piece = False
        self.square.piece = None

        self.board.get_square(pos).has_piece = True
        self.board.get_square(pos).piece = self

    def capture(self, piece):
        pass

    def die(self):
        pass

    def generate_moves(self):
        pass

import operator, pygame

from Board import Board, Square
from Utils.utils import add


class Piece(pygame.sprite.Sprite):
    def __init__(self, board: Board.Board, square: Square.Square, color: bool, image: str):
        super().__init__()
        self.pos = square.pos
        self.game_pos = self.pos[0] // 80, self.pos[1] // 80
        self.board = board
        self.square = square
        self.piece_moves = []
        self.color = color  # True is white, False is black
        self.image = pygame.image.load(self.load_resource(color, image))
        square.piece = self
        square.has_piece = True
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    @staticmethod
    def load_resource(color: bool, name: str):
        return "textures/" + ("w" if color else "b") + name + ".png"

    def can_capture(self, pos: tuple) -> bool:
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

    def generate_moves(self) -> list:
        return []

    def on_select(self):
        moves = self.generate_moves()
        for i in moves:
            self.board.get_square(i).color = (255, 0, 0)

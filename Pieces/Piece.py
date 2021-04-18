import operator
import pygame

from Bonuses import Bonus

from Board import Board, Square


class Piece(pygame.sprite.Sprite):
    def __init__(self, board: Board.Board, square: Square.Square, color: bool, image: str):
        super().__init__()
        self.pos = square.pos
        self.game_pos = self.pos[0] // 80, self.pos[1] // 80
        self.board = board
        self.square = square
        self.color = color  # True is white, False is black
        self.image = pygame.image.load(self.load_resource(color, image))
        square.piece = self
        square.has_piece = True
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.moves = self.generate_moves()
        self.bonuses = {}

    @staticmethod
    def load_resource(color: bool, name: str):
        return "textures/" + ("w" if color else "b") + name + ".png"

    def can_capture(self, pos: tuple) -> bool:
        return self.board.get_square(pos).has_piece and self.board.get_square(pos).piece.color is not self.color

    def can_capture_(self, pos: tuple) -> bool:
        self.moves = self.generate_moves()
        return self.board.get_square(pos).has_piece and self.board.get_square(pos).piece.color is not self.color and pos in self.moves

    # def can_move(self, pos: tuple) -> bool:
    #     possible_locs = [add(self.pos, move) for move in self.piece_moves]
    #     if any(pos == i for i in possible_locs):
    #         if any(self.board.get_square(i).has_piece for i in possible_locs):
    #             return False
    #     return True

    def move(self, newpos: tuple):
        self.game_pos = newpos
        self.update_piece()
        self.square.has_piece = False
        self.square.piece = None
        if self.board.get_square(newpos).has_piece:
            self.capture(newpos)
        else:
            self.board.get_square(newpos).has_piece = True
            self.board.get_square(newpos).piece = self
            self.square = self.board.get_square(newpos)
        self.moves = self.generate_moves()

    def capture(self, pos):
        self.board.get_square(pos).piece.kill()
        self.board.get_square(pos).has_piece = True
        self.board.get_square(pos).piece = self
        self.square = self.board.get_square(pos)

    def die(self):
        pass

    def generate_moves(self) -> list:
        return []

    def on_select(self):
        self.generate_moves()
        for i in self.moves:
            self.board.screen.blit(self.board.get_square(
                i).image, self.board.get_square(i).pos)

    def can_move(self, newpos):
        return self.board.get_square(newpos).has_piece and newpos != self.pos and self.can_capture(newpos)

    def update_piece(self):
        self.moves = self.generate_moves()

        self.pos = self.game_pos[0] * 80, self.game_pos[1] * 80
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

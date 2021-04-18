import pygame

from CBoard import Board, Square


class Piece(pygame.sprite.Sprite):
    def __init__(self, board: Board, square: Square.Square, color: bool, image: str):
        super().__init__()
        self.color = color
        self.value = 0
        self.has_moved = False
        self.pos = square.pos
        self.board = board
        self.bonuses = {}
        self.square = square
        self.image = pygame.image.load(self.load_resource(color, image))
        self.square.piece = self
        self.square.has_piece = True
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.game_pos = (self.pos[0] // 80, self.pos[1] // 80)
        self.moves = []

    @staticmethod
    def load_resource(color: bool, name: str):
        return "textures/" + ("w" if color else "b") + name + ".png"

    def can_capture(self, pos: tuple) -> bool:
        return self.board.get_square(pos).has_piece and self.board.get_square(pos).piece.color is not self.color

    def can_capture_(self, pos: tuple) -> bool:
        return self.board.get_square(pos).has_piece and self.board.get_square(pos).piece.color is not self.color and pos in self.moves

    def move(self, newpos: tuple):
        self.has_moved = True
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

    def move_val(self, newpos: tuple) -> int:
        val = 0
        square = self.board.get_square(newpos)
        if square.has_piece:
            if square.piece.color is not self.color:
                val = square.piece.value
        return self.board.calculate_value() - val

    def capture(self, pos):
        self.board.get_square(pos).piece.kill()
        self.board.get_square(pos).has_piece = True
        self.board.get_square(pos).piece = self
        self.square = self.board.get_square(pos)

    def generate_moves(self) -> list:
        return []

    def on_select(self):
        for i in self.moves:
            self.board.screen.blit(self.board.get_square(i).image, self.board.get_square(i).pos)

    def can_move(self, newpos):
        return self.board.get_square(newpos).has_piece and newpos != self.pos and self.can_capture(newpos)

    def update_piece(self):
        self.moves = self.generate_moves()
        self.pos = self.game_pos[0] * 80, self.game_pos[1] * 80
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.unique_update()

    def unique_update(self):
        pass

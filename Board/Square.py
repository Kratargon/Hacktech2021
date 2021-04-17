import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, color, multiplier: int):
        super().__init__()
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.piece = None
        self.has_piece = False
        self.board_pos = pos[0], pos[1]
        self.color = color
        self.rect = pygame.rect.Rect(self.board_pos, (multiplier * 10, multiplier * 10))


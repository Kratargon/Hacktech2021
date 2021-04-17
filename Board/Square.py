import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, color, multiplier: int):
        super().__init__()
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.piece = None
        self.has_piece = False
        self.board_pos = pos[0] // 80, pos[1] // 80
        self.color = color
        self.rect = pygame.rect.Rect(self.pos, (multiplier * 10, multiplier * 10))
        self.image = pygame.Surface((multiplier * 10, multiplier * 10))
        self.image.fill((255, 0, 0))
        self.image.set_alpha(128)
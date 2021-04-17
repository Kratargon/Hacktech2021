class Square:
    def __init__(self, pos: tuple):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.piece = None
        self.has_piece = False

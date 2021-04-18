import Pieces


class Bonus:
    def __init__(self):
        self.tuples = []
        self.pieces = []


class Diagonal(Bonus):
    def __init__(self):
        super().__init__()
        self.tuples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.pieces = [Pieces.Knight, Pieces.Rook]


class Horizontal(Bonus):
    def __init__(self):
        super().__init__()
        self.tuples = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.pieces = [Pieces.Knight, Pieces.Bishop]


class Knighted(Bonus):
    def __init__(self):
        super().__init__()
        self.tuples = [(-2, -1), (-1, -2), (1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2)]
        self.pieces = [Pieces.King, Pieces.Queen]


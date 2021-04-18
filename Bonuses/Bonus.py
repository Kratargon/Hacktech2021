import Pieces


class Diagonal:
    def __init__(self):
        self.tuples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.pieces = [Pieces.Knight, Pieces.Rook]


class Horizontal:
    def __init__(self):
        self.tuples = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.pieces = [Pieces.Knight, Pieces.Bishop]


class Knighted:
    def __init__(self):
        self.tuples = [(-2, -1), (-1, -2), (1, 2), (2, 1),
                       (-1, 2), (-2, 1), (2, -1), (1, -2)]
        self.pieces = [Pieces.King, Pieces.Queen]


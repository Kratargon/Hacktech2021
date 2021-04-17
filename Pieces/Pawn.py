from Pieces import Piece


class Pawn(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)
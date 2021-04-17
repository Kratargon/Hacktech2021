from Pieces import Piece


class Knight(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)

        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                self.piece_moves.append((i, j))

        for i in range(-1, 2, 2):
            for j in range(-2, 3, 4):
                self.piece_moves.append((i, j))


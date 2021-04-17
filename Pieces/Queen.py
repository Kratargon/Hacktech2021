from Pieces import Piece


class Queen(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)

        for i in range(board.size):
            # vertical moves
            self.piece_moves.append((0, i))
            self.piece_moves.append((0, -i))

            # horizontal moves
            self.piece_moves.append((i, 0))
            self.piece_moves.append((-i, 0))

            # diagonal moves
            self.piece_moves.append(i, i)
            self.piece_moves.append(i, -i)
            self.piece_moves.append(-i, i)
            self.piece_moves.append(-i, -i)
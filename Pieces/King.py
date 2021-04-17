from Pieces import Piece


class King(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)
        self.has_moved = False
        self.piece_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def in_check(self) -> bool:
        return any(True is i.can_capture(self.square.pos) for i in self.board.get_enemy_pieces(self.color))

    def checkmate(self) -> bool:
        for move in self.piece_moves:
            if self.can_move(self.board.get_square(self.square.pos + move)):
                return False

        return True


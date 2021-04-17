from Pieces import Piece
from Utils.utils import add


class Pawn(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)
        self.piece_moves = [(0, 1)]
        self.capture_moves = [(1, 1), (-1, 1)]
        self.first_turn = False

    def generate_moves(self):
        moves = []
        if self.first_turn:
            moves.append(add(self.pos, (0, 2)))

        newpos = add(self.pos, (0, 1))
        if self.board.check_bounds(newpos):
            moves.append(newpos)

        return newpos

    # todo: pawn capturing


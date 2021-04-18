from Pieces import Piece
from Utils.utils import add


class Pawn(Piece.Piece):
    def __init__(self, board, square, color):
        self.first_turn = False
        super().__init__(board, square, color, "pawn")

    def generate_moves(self):
        moves = []
        if self.first_turn:
            moves.append(add(self.pos, (0, 2)))

        newpos = add(self.pos, (0, 1))
        if self.board.check_bounds(newpos) and not self.board.get_square(newpos).has_piece:
            moves.append(newpos)

        newpos = add(self.pos, (1, 1))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)

        newpos = add(self.pos, (-1, 1))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)

        return moves

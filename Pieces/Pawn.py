from Pieces import Piece
from Utils.utils import add


class Pawn(Piece.Piece):
    def __init__(self, board, square, color):
        self.value = 1
        super().__init__(board, square, color, "pawn")

    def generate_moves(self):
        moves = []
        movement = -1 if self.color else 1

        if not self.has_moved:
            if self.color:
                moves.append(add(self.game_pos, (0, -2)))
            else:
                moves.append(add(self.game_pos, (0, 2)))

        newpos = add(self.game_pos, (0, movement))
        if self.board.check_bounds(newpos) and not self.board.get_square(newpos).has_piece:
            moves.append(newpos)

        newpos = add(self.game_pos, (1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)

        newpos = add(self.game_pos, (-1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)
        return moves

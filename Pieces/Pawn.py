from Pieces import Piece
from Utils.utils import add


class Pawn(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "pawn")

    def generate_moves(self):
        self.moves = []
        movement = -1 if self.color else 1

        if not self.has_moved:
            if self.color:
                self.moves.append(add(self.game_pos, (0, -2)))
            else:
                self.moves.append(add(self.game_pos, (0, 2)))

        newpos = add(self.game_pos, (0, movement))
        if self.board.check_bounds(newpos) and not self.board.get_square(newpos).has_piece:
            self.moves.append(newpos)

        newpos = add(self.game_pos, (1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            self.moves.append(newpos)

        newpos = add(self.game_pos, (-1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            self.moves.append(newpos)
        return self.moves

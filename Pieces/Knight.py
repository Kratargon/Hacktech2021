from Pieces import Piece
from Utils.utils import add


class Knight(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "knight")

    def generate_moves(self):
        moves = []
        tuples = [(-2, -1), (-1, -2), (1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2)]
        for i in tuples:
            newpos = add(self.game_pos, i)
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                moves.append(newpos)

        self.moves = moves

        return moves

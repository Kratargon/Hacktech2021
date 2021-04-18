from Pieces import Piece
from Utils.utils import add
from Bonuses import Bonus


class Knight(Piece.Piece):
    def __init__(self, board, square, color, d: bool = None, h: bool = None):
        super().__init__(board, square, color, "knight")
        self.value = 3
        self.bonuses = {Bonus.Diagonal(): d, Bonus.Horizontal(): h}

    def generate_moves(self):
        moves = []
        tuples = [(-2, -1), (-1, -2), (1, 2), (2, 1),
                  (-1, 2), (-2, 1), (2, -1), (1, -2)]
        for i in tuples:
            newpos = add(self.game_pos, i)
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                else:
                    moves.append(newpos)
        tuples = []
        for key, value in self.bonuses.items():

            if value is True:
                tuples += key.tuples
        for i in tuples:
            i = add(self.game_pos, i)
            if self.board.check_bounds(i):
                if self.board.get_square(i).has_piece and i != self.game_pos:
                    if self.can_capture(i):
                        moves.append(i)
                else:
                    moves.append(i)
        return moves

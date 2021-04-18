from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class Rook(Piece.Piece):
    def __init__(self, board, square, color, d: bool = False, k: bool = False):
        self.value = 5
        super().__init__(board, square, color, "rook")
        self.bonuses = {Bonus.Diagonal(): d, Bonus.Knighted(): k}

    def generate_moves(self):
        self.moves = []
        self.smolFunction(0, 1)
        self.smolFunction(0, -1)
        self.smolFunction(1, 0)
        self.smolFunction(-1, 0)
        tuples = []
        for key, value in self.bonuses.items():
            if value is True:
                tuples += key.tuples
        for i in tuples:
            i = add(self.game_pos, i)
            if self.board.check_bounds(i):
                if self.board.get_square(i).has_piece and i != self.game_pos:
                    if self.can_capture_(i):
                        self.moves.append(i)
                else:
                    self.moves.append(i)
        return self.moves

    def smolFunction(self, x, y):
        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i * x, i * y))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    if self.can_capture(newpos):
                        self.moves.append(newpos)
                    break
                self.moves.append(newpos)

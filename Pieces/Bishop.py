from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class Bishop(Piece.Piece):
    def __init__(self, board, square, color, h: bool = None, k: bool = None):
        super().__init__(board, square, color, "bishop")
        self.bonuses = {Bonus.Horizontal(): h, Bonus.Knighted(): k}
        self.value = 3

    def generate_moves(self):
        moves = []
        tuples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for key, value in self.bonuses.items():
            if value is True:
                tuples += key.tuples
        for i in tuples:
            moves += self.smolFunction(i[0], i[1])

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

    def smolFunction(self, x, y):
        moves = []
        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i * x, i * y))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break

                moves.append(newpos)
        return moves

    def unique_update(self):
        pass
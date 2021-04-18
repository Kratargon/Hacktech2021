from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class Bishop(Piece.Piece):
    def __init__(self, board, square, color):
        self.bonuses = {Bonus.Horizontal(): True, Bonus.Knighted(): False}
        self.value = 3
        super().__init__(board, square, color, "bishop")

    def generate_moves(self):
        moves = []
        tuples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for key, value in self.bonuses.items():
            if value is True:
                tuples += key.tuples
        for i in tuples:
            moves += self.smolFunction(i[0], i[1])

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
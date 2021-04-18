from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class Bishop(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "bishop")
        self.bonuses = {Bonus.Horizontal: False, Bonus.Knighted: False}


    def generate_moves(self):
        self.moves = []

        self.smolFunction(1, 1)
        self.smolFunction(1, -1)
        self.smolFunction(-1, 1)
        self.smolFunction(-1, -1)

    def smolFunction(self, x, y):
        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i * x, i * y))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    if self.can_capture(newpos):
                        self.moves.append(newpos)
                    break
                self.moves.append(newpos)

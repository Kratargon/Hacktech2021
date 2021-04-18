from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class King(Piece.Piece):
    def __init__(self, board, square, color):
        self.has_moved = False
        self.bonuses = {Bonus.Knighted(): False}
        super().__init__(board, square, color, "king")

    def in_check(self, pos=None) -> bool:
        if pos is None:
            pos = self.game_pos
        ls = []
        for piece in self.board.get_enemy_pieces(self.color):
            ls.append(piece.can_capture_(self.game_pos))
            # ls.append(any(self.game_pos == i for i in piece.moves))
        return any(ls)

    def checkmate(self) -> bool:
        possible_moves = [i for i in self.moves]
        fail = []
        for i in possible_moves:
            if self.in_check(i):
                fail.append(True)
            else:
                fail.append(False)
        if self.in_check():
            fail.append(True)
        return all(fail)

    def generate_moves(self):
        self.moves = [(1, 0), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        return self.moves

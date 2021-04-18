from Bonuses import Bonus
from Pieces import Piece, Pawn
from Utils.utils import add
import Pieces


class King(Piece.Piece):
    def __init__(self, board, square, color, k: bool = None):
        super().__init__(board, square, color, "king")
        self.value = 100
        self.bonuses = {Bonus.Knighted(): k}

    def in_check(self) -> bool:
        return any(piece.can_capture_(self.game_pos) for piece in self.board.get_enemy_pieces(self.color))

    def check_if_check(self, pos) -> bool:
        res = []
        for piece in self.board.get_enemy_pieces(self.color):
            if isinstance(piece, Pieces.Pawn):
                temp_moves = piece.simulate_capture(pos)
            else:
                temp_moves = piece.moves
            res.append(any(pos == move for move in list(set(temp_moves))))

        return any(res)

    def generate_moves(self):
        tuples = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (-1, 1), (-1, -1), (1, 1), (1, -1)]
        moves = []
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

        # for i in moves:
        #     if self.check_if_check(i):
        #         moves.remove(i)
        return moves

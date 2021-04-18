from Bonuses import Bonus
from Pieces import Piece, Pawn
from Utils.utils import add
import Pieces


class King(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "king")
        self.value = 100
        self.bonuses = {Bonus.Knighted(): False}

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
        tuples = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        moves = []
        for i in tuples:
            newpos = add(self.game_pos, i)
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                else:
                    moves.append(newpos)

        for i in moves:
            print(moves)
            if self.check_if_check(i):
                moves.remove(i)
                print("here")
        return moves

    def unique_update(self):
        if self.in_check():
            print("I'm in check!!!!!")
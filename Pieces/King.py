from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class King(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "king")
        self.value = 100
        self.bonuses = {Bonus.Knighted(): False}

    def in_check(self, pos=None) -> bool:
        if pos is None:
            pos = self.game_pos
        for piece in self.board.get_enemy_pieces(self.color):
            if piece.can_capture(pos):
                print(piece.game_pos)
        return any(piece.can_capture(pos) for piece in self.board.get_enemy_pieces(self.color))

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

        return moves

    def unique_update(self):
        if self.in_check():
            print("I'm in check!!!!!")
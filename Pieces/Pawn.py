from Bonuses import Bonus
from Pieces import Piece
import Pieces


from Utils.utils import add


class Pawn(Piece.Piece):
    def __init__(self, board, square, color, k):
        super().__init__(board, square, color, "pawn")
        self.queen_upgrades = {Bonus.Knighted(): k}
        self.qupgrade = k
        self.value = 1

    def generate_moves(self):
        moves = []
        movement = -1 if self.color else 1

        if not self.has_moved:
            if self.color:
                moves.append(add(self.game_pos, (0, -2)))
            else:
                moves.append(add(self.game_pos, (0, 2)))

        newpos = add(self.game_pos, (0, movement))
        if self.board.check_bounds(newpos) and not self.board.get_square(newpos).has_piece:
            moves.append(newpos)

        newpos = add(self.game_pos, (1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)

        newpos = add(self.game_pos, (-1, movement))
        if self.board.check_bounds(newpos) and self.can_capture(newpos):
            moves.append(newpos)
        return moves

    def simulate_capture(self, newpos: tuple):
        movement = -1 if self.color else 1
        temp = [add(self.game_pos, (1, movement)),
                add(self.game_pos, (-1, movement))]

        return temp

    def unique_update(self):
        if self.game_pos[1] == (0 if self.color else self.board.size - 1):
            self.promote()
            self.kill()

    def promote(self):
        print(self.game_pos)
        print(self.square.pos)
        print(self.board.get_square(self.game_pos).pos)
        if self.color:
            piece = Pieces.Queen(self.board, self.board.get_square(
                self.game_pos), self.color, self.qupgrade)
            self.board.white_pieces.add(piece)
            print(piece)
        else:
            self.board.black_pieces.add(Pieces.Queen(
                self.board, self.board.get_square(self.game_pos), self.color, self.qupgrade))

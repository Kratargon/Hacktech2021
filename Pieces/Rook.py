from Pieces import Piece
from Utils.utils import add


class Rook(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "rook")

    def generate_moves(self):
        moves = []

        # down
        for i in range(self.game_pos[1], self.board.size, 1):
            newpos = add(self.game_pos, (0, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        # up
        for i in range(self.game_pos[1], -1, -1):
            newpos = add(self.game_pos, (0, -i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        # right
        for i in range(self.game_pos[0], self.board.size, 1):
            newpos = add(self.game_pos, (i, 0))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        # left
        for i in range(self.game_pos[0], -1, -1):
            newpos = add(self.game_pos, (-i, 0))
            if self.board.get_square(newpos).has_piece and newpos != self.pos:
                if self.can_capture(newpos):
                    moves.append(newpos)
                break
            moves.append(newpos)

        return moves



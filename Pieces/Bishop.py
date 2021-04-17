from Pieces import Piece
from Utils.utils import add


class Bishop(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "bishop")

    def generate_moves(self):
        moves = []

        # up right
        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i, -i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (-i, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (-i, -i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)
        return moves

from Pieces import Piece
from Utils.utils import add


class Bishop(Piece.Piece):
    def __init__(self, board, square):
        super().__init__(board, square)

    def generate_moves(self):
        moves = []

        # up right
        for i in range(self.pos[0], self.board.size, 1):
            newpos = add(self.pos, (i, i))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
            if self.board.get_square(newpos).has_piece:
                break

        # left
        for i in range(self.board.size, self.pos[0], -1):
            newpos = add(self.pos, (0, i))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
            if self.board.get_square(newpos).has_piece:
                break

        # up
        for i in range(self.pos[1], self.board.size, 1):
            newpos = add(self.pos, (i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
            if self.board.get_square(newpos).has_piece:
                break

        # down
        for i in range(self.board.size, self.pos[1], -1):
            newpos = add(self.pos, (i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
            if self.board.get_square(newpos).has_piece:
                break
        return moves

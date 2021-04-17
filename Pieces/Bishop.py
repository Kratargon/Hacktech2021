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
                moves.append(newpos)
                print(newpos)
                if self.board.get_square(newpos).has_piece:
                    break

            newpos = add(self.game_pos, (i, -i))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                if self.board.get_square(newpos).has_piece:
                    break

            newpos = add(self.game_pos, (-i, i))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                if self.board.get_square(newpos).has_piece:
                    break

            newpos = add(self.game_pos, (-i, -i))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                if self.board.get_square(newpos).has_piece:
                    break
        return moves

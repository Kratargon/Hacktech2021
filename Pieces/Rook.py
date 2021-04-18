from Bonuses import Bonus
from Pieces import Piece


class Rook(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "rook")
        self.bonuses = {Bonus.Knighted(): True, Bonus.Diagonal(): False}

    def generate_moves(self):
        moves = []

        # down
        for i in range(self.game_pos[1], self.board.size, 1):
            newpos = self.game_pos[0], i
            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # up
        for i in range(self.game_pos[1], -1, -1):
            newpos = self.game_pos[0], i

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # right
        for i in range(self.game_pos[0], self.board.size, 1):
            newpos = i, self.game_pos[1]

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # left
        for i in range(self.game_pos[0], -1, -1):
            newpos = i, self.game_pos[1]

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        return moves

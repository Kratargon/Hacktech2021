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
                moves.append(newpos)
                # print("in down: appending", newpos, self.game_pos)

                if self.board.get_square(newpos).has_piece:
                    break
        print("out of first")

        # up
        for i in range(self.game_pos[1], -1, -1):
            newpos = add(self.game_pos, (0, -i))
            print(newpos)
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                # print("in up: appending", newpos, self.game_pos)

                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    break
        print("out of second")

        # right
        for i in range(self.game_pos[0], self.board.size, 1):
            newpos = add(self.game_pos, (i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                # print("in right: appending", newpos, self.game_pos)

                if self.board.get_square(newpos).has_piece:
                    break

        print("out of third")

        # left
        for i in range(self.game_pos[0], -1, -1):
            newpos = add(self.game_pos, (-i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)
                # print("in left: appending", newpos, self.game_pos)
                if self.board.get_square(newpos).has_piece:
                    break

        print("out of fourtH")
        print(moves)
        return moves



import operator

from Pieces import Piece
from Utils.utils import add


class King(Piece.Piece):
    def __init__(self, board, square, color):
        super().__init__(board, square, color, "king")
        self.has_moved = False
        self.piece_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def in_check(self) -> bool:
        return any(True is i.can_capture(self.square.pos) for i in self.board.get_enemy_pieces(self.color))

    def checkmate(self) -> bool:
        for move in self.piece_moves:
            if self.can_move(self.board.get_square(tuple(map(operator.add, self.pos, move)))):
                return False
        return True

    def generate_moves(self):
        moves = []

        # up right
        for i in range(-1, 1 + 1):
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

        for i in range(-1, 2):
            newpos = add(self.game_pos, (0, i))
            print(newpos)
            if self.board.check_bounds(newpos):
                moves.append(newpos)

                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    break

            newpos = add(self.game_pos, (0, -i))
            print(newpos)
            if self.board.check_bounds(newpos):
                moves.append(newpos)

                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    break

        for i in range(-1, 2):
            newpos = add(self.game_pos, (i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)

                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    break

        for i in range(-1, 2):
            newpos = add(self.game_pos, (-i, 0))
            if self.board.check_bounds(newpos):
                moves.append(newpos)

                if self.board.get_square(newpos).has_piece and newpos != self.game_pos:
                    break

        return moves

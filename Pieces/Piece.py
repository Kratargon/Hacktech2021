from Board import Board, Square


class Piece:
    def __init__(self, board: Board.Board, square: Square.Square):
        self.board = board
        self.square = square
        self.piece_moves = []
        self.color = None
        square.piece = self

    def can_capture(self, square: Square.Square) -> bool:
        return False

    def can_move(self, square: Square.Square) -> bool:
        pass

    def move(self, square: Square.Square):
        pass

    def capture(self, piece):
        pass

    def die(self):
        pass

    def add_move(self, move: tuple) -> None:
        self.piece_moves.append(move)

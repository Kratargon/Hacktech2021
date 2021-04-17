from Board import Square


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [list() * size]

    def get_square(self, pos: tuple) -> Square.Square:
        return self.board[pos[1]][pos[0]]

from CBoard import Board
import Pieces
from Pieces import white, black


class Bounds:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = y


def gen_board(board: Board, dupgrades, hupgrades, kupgrades):
    size = Bounds(0, board.size)
    gen_pawns(board)
    for i in range(board.size // 2 - 1):

        if i % 2 == 0 and i % 4:
            gen_bishops(board, size, i, True if "bishop" in hupgrades else False, True if "bishop" in kupgrades else False)
        elif i % 2 != 0 and i % 3:
            gen_knights(board, size, i, True if "knight" in dupgrades else False, True if "knight" in hupgrades else False)
        else:
            gen_rooks(board, size, i, True if "rook" in dupgrades else False, True if "rook" in kupgrades else False)

    gen_queens(board, True if "queen" in kupgrades else False)
    kings = gen_kings(board, True if "king" in kupgrades else False)
    return kings


def gen_pawns(board: Board):
    for i in range(board.size):
        board.white_pieces.add(Pieces.Pawn(board, board.get_square((i, board.size - 2)), white))
        board.black_pieces.add(Pieces.Pawn(board, board.get_square((i, 1)), black))


def gen_rooks(board: Board, size, i, d: bool = None, k: bool = None):
    board.white_pieces.add(Pieces.Rook(board, board.get_square((i, size.y - 1)), white, d, k))
    board.white_pieces.add(Pieces.Rook(board, board.get_square((size.size - i - 1, size.y - 1)), white, d, k))

    board.black_pieces.add(Pieces.Rook(board, board.get_square((i, 0)), black))
    board.black_pieces.add(Pieces.Rook(board, board.get_square((size.size - i - 1, 0)), black))


def gen_knights(board: Board, size, i, d, h):
    board.white_pieces.add(Pieces.Knight(board, board.get_square((i, size.y - 1)), white, d, h))
    board.white_pieces.add(Pieces.Knight(board, board.get_square((size.size - i - 1, size.y - 1)), white, d, h))

    board.black_pieces.add(Pieces.Knight(board, board.get_square((i, 0)), black))
    board.black_pieces.add(Pieces.Knight(board, board.get_square((size.size - i - 1, 0)), black))


def gen_bishops(board: Board, size, i, h, k):
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((i, size.y - 1)), white, h, k))
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((size.size - i - 1, size.y - 1)), white, h, k))

    board.black_pieces.add(Pieces.Bishop(board, board.get_square((i, 0)), black))
    board.black_pieces.add(Pieces.Bishop(board, board.get_square((size.size - i - 1, 0)), black))


def gen_queens(board: Board, k):
    board.white_pieces.add(Pieces.Queen(board, board.get_square((board.size // 2 - 1, board.size - 1)), white, k))
    board.black_pieces.add(Pieces.Queen(board, board.get_square((board.size // 2 - 1, 0)), black))


def gen_kings(board: Board, k):
    kings = {"white": Pieces.King(board, board.get_square((board.size // 2, board.size - 1)), white, k), "black": Pieces.King(board, board.get_square((board.size // 2, 0)), black)}

    board.white_pieces.add(kings["white"])
    board.black_pieces.add(kings["black"])
    return kings
from CBoard import Board
import Pieces
from Pieces import white, black


class Bounds:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = y


def gen_board(board: Board, wdupgrades, whupgrades, wkupgrades, bdupgrades, bhupgrades, bkupgrades):
    size = Bounds(0, board.size)
    gen_pawns(board)
    for i in range(board.size // 2 - 1):
        if i % 3 == 0:
            gen_rooks(board, size, i, True if "rook" in wdupgrades else False, True if "rook" in wkupgrades else False,
                      True if "rook" in bdupgrades else False, True if "rook" in bkupgrades else False)
        elif (i - 1) % 3 == 0 or i == 1:
            gen_knights(board, size, i, True if "knight" in wdupgrades else False, True if "knight" in whupgrades else
            False, True if "knight" in bdupgrades else False, True if "knight" in bhupgrades else False)
        elif (i - 2) % 3 == 0 or i == 2:
            gen_bishops(board, size, i, True if "bishop" in whupgrades else False, True if "bishop" in wkupgrades else
            False, True if "bishop" in bhupgrades else False, True if "bishop" in bkupgrades else False)

    gen_queens(board, True if "queen" in wkupgrades else False, True if "queen" in bkupgrades else False)
    kings = gen_kings(board, True if "king" in wkupgrades else False, True if "king" in bkupgrades else False)
    return kings


def gen_pawns(board: Board):
    for i in range(board.size):
        board.white_pieces.add(Pieces.Pawn(board, board.get_square((i, board.size - 2)), white))
        board.black_pieces.add(Pieces.Pawn(board, board.get_square((i, 1)), black))


def gen_rooks(board: Board, size, i, wd: bool = None, wk: bool = None, bd: bool = None, bk: bool = None):
    board.white_pieces.add(Pieces.Rook(board, board.get_square((i, size.y - 1)), white, wd, wk))
    board.white_pieces.add(Pieces.Rook(board, board.get_square((size.size - i - 1, size.y - 1)), white, wd, wk))

    board.black_pieces.add(Pieces.Rook(board, board.get_square((i, 0)), black, bd, bk))
    board.black_pieces.add(Pieces.Rook(board, board.get_square((size.size - i - 1, 0)), black, bd, bk))


def gen_knights(board: Board, size, i, wd, wh, bd, bh):
    board.white_pieces.add(Pieces.Knight(board, board.get_square((i, size.y - 1)), white, wd, wh))
    board.white_pieces.add(Pieces.Knight(board, board.get_square((size.size - i - 1, size.y - 1)), white, wd, wh))

    board.black_pieces.add(Pieces.Knight(board, board.get_square((i, 0)), black, bd, bh))
    board.black_pieces.add(Pieces.Knight(board, board.get_square((size.size - i - 1, 0)), black, bd, bh))


def gen_bishops(board: Board, size, i, wh, wk, bh, bk):
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((i, size.y - 1)), white, wh, wk))
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((size.size - i - 1, size.y - 1)), white, wh, wk))

    board.black_pieces.add(Pieces.Bishop(board, board.get_square((i, 0)), black, bh, bk))
    board.black_pieces.add(Pieces.Bishop(board, board.get_square((size.size - i - 1, 0)), black, bh, bk))


def gen_queens(board: Board, wk, bk):
    board.white_pieces.add(Pieces.Queen(board, board.get_square((board.size // 2 - 1, board.size - 1)), white, wk))
    board.black_pieces.add(Pieces.Queen(board, board.get_square((board.size // 2 - 1, 0)), black, bk))


def gen_kings(board: Board, k, bk):
    kings = {"white": Pieces.King(board, board.get_square((board.size // 2, board.size - 1)), white, k), "black": Pieces.King(board, board.get_square((board.size // 2, 0)), black, bk)}

    board.white_pieces.add(kings["white"])
    board.black_pieces.add(kings["black"])
    return kings
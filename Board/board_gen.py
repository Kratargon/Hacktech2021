from Board import Board
import Pieces


def gen_board(board: Board):
    gen_pawns(board)
    gen_rooks(board)
    gen_knights(board)
    gen_bishops(board)
    gen_royals(board)


def gen_pawns(board: Board):
    for i in range(board.size):
        board.white_pieces.add(Pieces.Pawn(board, board.get_square((i, 1)), False))
        board.black_pieces.add(Pieces.Pawn(board, board.get_square((i, board.size - 2)), True))


def gen_rooks(board: Board):
    board.white_pieces.add(Pieces.Rook(board, board.get_square((0, 7)), True))
    board.white_pieces.add(Pieces.Rook(board, board.get_square((7, 7)), True))

    board.black_pieces.add(Pieces.Rook(board, board.get_square((0, 0)), False))
    board.black_pieces.add(Pieces.Rook(board, board.get_square((7, 0)), False))


def gen_knights(board: Board):
    board.white_pieces.add(Pieces.Knight(board, board.get_square((1, 7)), True))
    board.white_pieces.add(Pieces.Knight(board, board.get_square((6, 7)), True))

    board.black_pieces.add(Pieces.Knight(board, board.get_square((1, 0)), False))
    board.black_pieces.add(Pieces.Knight(board, board.get_square((6, 0)), False))


def gen_bishops(board: Board):
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((2, 7)), True))
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((5, 7)), True))

    board.black_pieces.add(Pieces.Bishop(board, board.get_square((2, 0)), False))
    board.black_pieces.add(Pieces.Bishop(board, board.get_square((5, 0)), False))


def gen_royals(board: Board):
    board.white_pieces.add(Pieces.Queen(board, board.get_square((3, 7)), True))
    board.white_pieces.add(Pieces.King(board, board.get_square((4, 7)), True))

    board.black_pieces.add(Pieces.Queen(board, board.get_square((4, 0)), False))
    board.white_pieces.add(Pieces.King(board, board.get_square((3, 0)), False))

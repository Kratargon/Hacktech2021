from CBoard import Board
import Pieces
from Pieces import white, black


def gen_board(board: Board):
    gen_pawns(board)
    gen_rooks(board)
    gen_knights(board)
    gen_bishops(board)
    gen_queens(board)


def gen_pawns(board: Board):
    for i in range(board.size):
        board.white_pieces.add(Pieces.Pawn(board, board.get_square((i, board.size - 2)), white))
        board.black_pieces.add(Pieces.Pawn(board, board.get_square((i, 1)), black))


def gen_rooks(board: Board):
    board.white_pieces.add(Pieces.Rook(board, board.get_square((0, 7)), white))
    board.white_pieces.add(Pieces.Rook(board, board.get_square((7, 7)), white))

    board.black_pieces.add(Pieces.Rook(board, board.get_square((0, 0)), black))
    board.black_pieces.add(Pieces.Rook(board, board.get_square((7, 0)), black))


def gen_knights(board: Board):
    board.white_pieces.add(Pieces.Knight(board, board.get_square((1, 7)), white))
    board.white_pieces.add(Pieces.Knight(board, board.get_square((6, 7)), white))

    board.black_pieces.add(Pieces.Knight(board, board.get_square((1, 0)), black))
    board.black_pieces.add(Pieces.Knight(board, board.get_square((6, 0)), black))


def gen_bishops(board: Board):
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((2, 7)), white))
    board.white_pieces.add(Pieces.Bishop(board, board.get_square((5, 7)), white))

    board.black_pieces.add(Pieces.Bishop(board, board.get_square((2, 0)), black))
    board.black_pieces.add(Pieces.Bishop(board, board.get_square((5, 0)), black))


def gen_queens(board: Board):
    board.white_pieces.add(Pieces.Queen(board, board.get_square((3, 7)), white))
    board.black_pieces.add(Pieces.Queen(board, board.get_square((4, 0)), black))

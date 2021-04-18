from Board import Board
import Pieces


def gen_pawns(board: Board):
    for i in range(board.size):
        board.white_pieces.add(Pieces.Pawn(board, board.get_square((i, 1)), False))
    #
    # for i in range(board.size):
        board.black_pieces.add(Pieces.Pawn(board, board.get_square((i, board.size - 2)), True))

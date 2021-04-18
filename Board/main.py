import pygame

from Board import Board
import Pieces


def gen_pawns():
    for i in range(board.size):
        Pieces.Pawn(board, board.get_square(2, i), True)

    for i in range(board.size):
        Pieces.Pawn(board, board.get_square(board.size - 2, i), False)

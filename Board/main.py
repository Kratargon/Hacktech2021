import pygame

from Board import Board
import Pieces

def gen_pawns():
    for i in range(board.size):
        Pieces.Pawn(board, board.get_square(1, i), True)

    for i in range(board.size):
        Pieces.Pawn(board, board.get_square(board.size - 2, i), False)

def gen_bishops():
    Pieces.Bishop(board, board.get_square(0, board.size - 3), True)
    Pieces.Bishop(board, board.get_square(0, 3), True)
    Pieces.Bishop(board, board.get_square(board.size - 1, board.size - 3), False)
    Pieces.Bishop(board, board.get_square(board.size - 1, 3), False)

def gen_knights():
    Pieces.Bishop(board, board.get_square(0, board.size - 3))
    Pieces.Bishop(board, board.get_square(0, 3))
import pygame

from CBoard import Board
import Pieces
import random


def randFrom(moveList, weights):
    tot = 0
    for i in weights:
        tot += i
    temp = random.randint(0, tot)
    tmp = 0
    for i in range(weights):
        tmp += weights[i]
        if temp < tmp:
            return moveList[i]

def createWeights(moveList, board):
    weights = []
    for i in moveList:
        weights.append(weightMove(i[0], i[1:-1], board))
    return weights

def weightMove(pieces, move, board):
    return piece.move_val(move) – board.calculate_value() + 40

def logicHandler(board):
    moveList = generateMoves(board)
    weights = createWeights(moveList, board)
    move = randFrom(moveList, weights)
    return move

def generateMoves(board):
    moveList = []
    for i in board.black_pieces:
        if i.has_move():
            moveList.append([i])
            for j in i.moves:
                moveList[-1].append(j)
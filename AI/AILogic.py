import pygame

from Board import Board
import Pieces
import Random

def randFrom(moveList, weights):
    tot = 0
    for i in weights:
        tot += i
    temp = randint(0, tot)
    tmp = 0
    for i in range(weights):
        tmp += weights[i]
        if temp < tmp:
            return moveList[i]
    return "ERROR"

def weightMove(move):
    return nextGameState(move) – currentGameState(move)
    #win = max_int, loss = 0, otherwise point value of my pieces - point value of enemy pieces
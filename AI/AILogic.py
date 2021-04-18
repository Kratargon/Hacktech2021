import random


def randFrom(moveList, weights):
    tot = 0
    for i in weights:
        tot += i
    temp = random.randint(0, tot)
    tmp = 0
    for i in range(len(weights)):
        tmp += weights[i]
        if temp < tmp:
            return moveList[i]


def createWeights(moveList, board):
    weights = []
    for i in moveList:
        weights.append(weightMove(i, board))
    return weights


def weightMove(move, board):
    return (move[0].move_val(move[1]) - board.calculate_value() + 40) ** 1000


def logicHandler(board):
    moveList = generateMoves(board)
    weights = createWeights(moveList, board)
    move = randFrom(moveList, weights)
    return move


def generateMoves(board):
    moveList = []
    for i in board.black_pieces:
        if i.has_move():
            for j in i.moves:
                moveList.append((i, j))

    return moveList

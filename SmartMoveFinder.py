import random

pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0


def findRandomMove(validMoves):
    print("Random")
    return validMoves[random.randint(0, len(validMoves)-1)]


def findBestMove(gs, validMoves):
    print("Best")

    trunMultiplier = 1 if gs.whiteToMove else -1
    random.shuffle(validMoves)
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None

    for playerMove in validMoves:
        print("in here")
        gs.makeMove(playerMove)
        opponentsMoves = gs.getAllValidMoves()
        opponentMaxScore = -CHECKMATE
        for opponentsMove in opponentsMoves:
            gs.makeMove(opponentsMove)
            if gs.checkMate:
                score = - trunMultiplier * CHECKMATE
            elif gs.staleMate:
                score = STALEMATE
            else:
                score = -trunMultiplier * scoreMaterial(gs.board)

            if score > opponentMaxScore:
                opponentMaxScore = score
            gs.undoMove()
        if(opponentMaxScore < opponentMinMaxScore):
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    print("best move is", bestPlayerMove)
    return bestPlayerMove


def scoreMaterial(board):

    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]

    print(score)
    return score

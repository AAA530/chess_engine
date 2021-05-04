import random

pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 2


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

        if gs.checkMate:
            opponentMaxScore = -CHECKMATE
        elif gs.staleMate:
            opponentMaxScore = STALEMATE
        else:
            opponentMaxScore = -CHECKMATE
            for opponentsMove in opponentsMoves:
                gs.makeMove(opponentsMove)
                gs.getAllValidMoves()
                if gs.checkMate:
                    score = CHECKMATE
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


def findBestMoveMinMax(gs, validMoves):
    global nextMove
    nextMove = None
    random.shuffle(validMoves)
    findMoveMinMax(gs, validMoves, DEPTH, gs.whiteToMove)
    return nextMove


def findMoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove
    if depth == 0:
        return scoreMaterial(gs.board)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getAllValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getAllValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore


"""
A Positive score is good for White, negative is good for black
"""


def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE  # Black Wins
        else:
            return CHECKMATE  # white wins
    elif gs.staleMate:
        return STALEMATE

    score = 0
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]

    print(score)
    return score


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

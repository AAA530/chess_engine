import sys
sys.path.append('')


from Chess import ChessEngine
import pygame as p


WIDTH = HEIGHT = 512

DIMENSION = 8

SQUARE_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK",
              "bp", "wp", "wR", "wN", "wB", "wQ", "wK"]

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(
            "images/"+piece+".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()

    print(gs.board)


main()

import pyxel

from .board import Board

class Chess:
    def __init__(self):
        pyxel.load('assets/chess.pyxres')
        pyxel.mouse(True)
        self.board = Board()

    def update(self):
        self.board.update()

    def draw(self):
        self.board.draw()

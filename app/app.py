import pyxel

from .chess import Chess


class App:
    def __init__(self):
        pyxel.init(128,128, title='chess', fps=60)
        self.game = Chess()


        pyxel.run(self.update, self.draw)

    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(0)
        self.game.draw()
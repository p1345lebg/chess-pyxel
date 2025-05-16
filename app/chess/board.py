import pyxel
from .chessObjects import *


class Board:
    def __init__(self):
        self.width : int = 8
        self.height : int = 8
        self.squareWidth = 16
        self.pieces : list[ChessPiece] = []
        self.moves : list[ChessMove] = []
        self.reset()

    @property
    def top_line(self) -> int:
        return 0
    @property
    def bottom_line(self) -> int:
        return self.height-1
    @property
    def left_line(self) -> int:
        return 0
    @property
    def right_line(self) -> int:
        return self.width-1

    def reset(self):
        self.pieces = []
        self.moves = []

        color = 7
        for i in range(self.width):
            self.pieces.append(Pawn(self, (i, 1), color, (0, 1)))

        self.pieces.append(Rook(self, (0, 0), color))
        self.pieces.append(Rook(self, (self.width - 1, 0), color))

        self.pieces.append(Bishop(self, (2, 0), color))
        self.pieces.append(Bishop(self, (self.width - 3, 0), color))

        self.pieces.append(Knight(self, (1, 0), color))
        self.pieces.append(Knight(self, (self.width - 2, 0), color))

        self.pieces.append(King(self, (3, 0), color))
        self.pieces.append(Queen(self, (self.width - 4, 0), color))

        color = 3
        for i in range(self.width):
            self.pieces.append(Pawn(self, (i, self.height - 2), color, (0, -1)))

        self.pieces.append(Rook(self, (0, self.height - 1), color))
        self.pieces.append(Rook(self, (self.width - 1, self.height - 1), color))

        self.pieces.append(Bishop(self, (2, self.height - 1), color))
        self.pieces.append(Bishop(self, (self.width - 3, self.height - 1), color))

        self.pieces.append(Knight(self, (1, self.height - 1), color))
        self.pieces.append(Knight(self, (self.width - 2, self.height - 1), color))

        self.pieces.append(King(self, (3, self.height - 1), color))
        self.pieces.append(Queen(self, (self.width - 4, self.height - 1), color))




    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for move in self.moves:
                if move.touch_cursor():
                    move.move_pawn()
                    return

            for piece in self.pieces:
                if piece.touch_cursor():
                    self.moves = piece.get_moves()
                    return


    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%2:
                    pyxel.rect(i*self.squareWidth,j*self.squareWidth, self.squareWidth, self.squareWidth, 4)
                else:
                    pyxel.rect(i*self.squareWidth,j*self.squareWidth, self.squareWidth, self.squareWidth, 9)

        for piece in self.pieces:
            piece.draw()

        for move in self.moves:
            move.draw()
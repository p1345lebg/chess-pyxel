import pyxel


class ChessObject:
    def __init__(self, board : "Board", coordinates : tuple[int,int]):
        self.board : "Board" = board
        self.coordinates : tuple[int,int] = coordinates

    def touch_cursor(self):
        if (self.board.squareWidth*self.coordinates[0] < pyxel.mouse_x < self.board.squareWidth*self.coordinates[0]+self.board.squareWidth and
            self.board.squareWidth*self.coordinates[1] < pyxel.mouse_y < self.board.squareWidth*self.coordinates[1]+self.board.squareWidth):
            return True
        return False


class ChessPiece(ChessObject):
    def __init__(self, board : "Board", coordinates : tuple[int,int],
                 color : int = 7):
        super().__init__(board=board, coordinates=coordinates)
        self.color : int = color
        self.textureIndex : int = 0

    def move(self, coordinates : tuple[int,int]):
        self.coordinates = coordinates

    def draw(self):
        pyxel.pal(7, self.color)
        pyxel.blt(x=self.board.squareWidth*self.coordinates[0],
                  y=self.board.squareWidth*self.coordinates[1],
                  img=0,
                  u=self.board.squareWidth*self.textureIndex,
                  v=0,
                  w=self.board.squareWidth,
                  h=self.board.squareWidth,
                  colkey=0)
        pyxel.pal()

    def get_moves(self) -> list["ChessMove"]:
        return []
import pyxel

from .chessObject import ChessObject


class ChessMove(ChessObject):
    def __init__(self, board : "Board", coordinates : tuple[int,int],
                 piece : "ChessPiece",
                 pieces_eat : list["ChessPiece"]|None = None):
        super().__init__(board=board, coordinates=coordinates)
        self.piece = piece
        self.piecesEat = pieces_eat if pieces_eat else []
        if self.piecesEat:
            self.r = 4
        else:
            self.r = 0

    def move_pawn(self) -> list["ChessObject"]:
        """
        deplace la pièce
        :return: retourne la liste des pieces mangées
        """
        self.piece.move(self.coordinates)
        for piece in self.piecesEat:
            if piece in self.board.pieces:
                self.board.pieces.remove(piece)
        self.board.moves = []

    def draw(self):
        pyxel.circb(self.coordinates[0]*self.board.squareWidth+self.board.squareWidth/2,
                    self.coordinates[1]*self.board.squareWidth+self.board.squareWidth/2,
                    self.r,
                    7)
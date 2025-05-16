from .chessObject import ChessPiece
from .chessMove import ChessMove

class Rook(ChessPiece):
    def __init__(self, board : "Board", coordinates : tuple[int,int], color : int = 7):
        super().__init__(board=board, coordinates=coordinates, color=color)
        self.textureIndex = 5

    def get_moves(self) -> list[ChessMove]:
        moves : list[ChessMove] = []
        pieces : dict[tuple[int,int],list["ChessPiece"]] = {}
        for piece in self.board.pieces:
            if piece is self:
                continue
            if piece.coordinates in pieces:
                pieces[piece.coordinates].append(piece)
            else:
                pieces[piece.coordinates] = [piece]

        directions = [
            (0, -1),  # haut
            (0, 1),  # bas
            (-1, 0),  # gauche
            (1, 0)  # droite
        ]

        x0, y0 = self.coordinates

        for dx, dy in directions:
            x, y = x0 + dx, y0 + dy
            while (self.board.left_line <= x <= self.board.right_line and
                   self.board.top_line <= y <= self.board.bottom_line):

                if (x, y) not in pieces:
                    moves.append(ChessMove(self.board, (x, y), self))
                elif all(piece.color == self.color for piece in pieces[(x,y)]):
                    break
                else:
                    moves.append(ChessMove(self.board, (x, y), self, pieces[(x, y)]))
                    break


                x += dx
                y += dy

        return moves




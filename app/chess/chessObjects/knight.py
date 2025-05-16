from .chessObject import ChessPiece
from .chessMove import ChessMove

class Knight(ChessPiece):
    def __init__(self, board: "Board", coordinates: tuple[int, int], color: int = 7):
        super().__init__(board=board, coordinates=coordinates, color=color)
        self.textureIndex = 4

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

        jumps = [
            (-2,-1),
            (-1,-2),
            (-2,1),
            (-1,2),
            (2,-1),
            (1,-2),
            (2,1),
            (1,2)
        ]

        x0, y0 = self.coordinates

        for jx, jy in jumps:
            x,y = x0+jx,y0+jy
            if (x,y) in pieces:
                if all(piece.color == self.color for piece in pieces[(x,y)]):
                    continue
                moves.append(ChessMove(self.board, (x,y), self, pieces[(x,y)]))
            elif (x < self.board.left_line or
                  x > self.board.right_line or
                  y < self.board.top_line or
                  y > self.board.bottom_line):
                continue
            else:
                moves.append(ChessMove(self.board, (x, y), self))



        return moves
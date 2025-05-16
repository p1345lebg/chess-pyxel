from .chessObject import ChessPiece
from .chessMove import ChessMove

class Pawn(ChessPiece):
    def __init__(self, board: "Board", coordinates: tuple[int, int], color: int = 7, finish_line_direction : tuple[int,int] = (0, -1)):
        super().__init__(board=board, coordinates=coordinates, color=color)
        self.finishLineDirection = finish_line_direction
        self.textureIndex = 6

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

        jump = self.finishLineDirection

        x, y = self.coordinates

        def out_of_limits(x_raciste, y_raciste) -> bool:
            if (x_raciste < self.board.left_line or
                x_raciste > self.board.right_line or
                y_raciste < self.board.top_line or
                y_raciste > self.board.bottom_line):
                return True
            return False


        x0, y0 = x + jump[0], y + jump[1]
        x1, y1 = x + jump[0]*2, y + jump[1]*2
        if (x0,y0) not in pieces and not out_of_limits(x0,y0):
            moves.append(ChessMove(self.board, (x0,y0), self))
            if (x1,y1) not in pieces and not out_of_limits(x1,y1):
                moves.append(ChessMove(self.board, (x1, y1), self))

        if abs(jump[0]) == abs(jump[1]):
            if (x0,y0) in pieces:
                moves.append(ChessMove(self.board, (x0, y0), self, pieces[(x0,y0)]))

        else:
            if self.finishLineDirection[0] == 0:
                if (not out_of_limits(x-1,y0) and
                    (x-1,y0) in pieces and
                    not all(piece.color == self.color for piece in pieces[(x-1,y0)])):
                    moves.append(ChessMove(self.board, (x-1, y0), self, pieces[(x-1, y0)]))
                if (not out_of_limits(x+1,y0) and
                    (x+1, y0) in pieces and
                    not all(piece.color == self.color for piece in pieces[(x+1, y0)])):
                    moves.append(ChessMove(self.board, (x+1, y0), self, pieces[(x+1, y0)]))
            elif self.finishLineDirection[1] == 0:
                if (not out_of_limits(x0,y-1) and
                    (x0,y-1) in pieces and
                    not all(piece.color == self.color for piece in pieces[(x0,y-1)])):
                    moves.append(ChessMove(self.board, (x0,y-1), self, pieces[(x0,y-1)]))
                if (not out_of_limits(x0,y+1) and
                    (x0,y+1) in pieces and
                    not all(piece.color == self.color for piece in pieces[(x0,y+1)])):
                    moves.append(ChessMove(self.board, (x0, y+1), self, pieces[(y+1, y0)]))

        return moves
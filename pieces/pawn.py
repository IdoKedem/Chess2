from board import Square
from .ibase_piece import IBasePiece


class Pawn(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

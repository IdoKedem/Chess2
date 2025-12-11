from base import IBasePiece
from board import Square


class Pawn(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

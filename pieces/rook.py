from base import IBasePiece
from board import Square


class Rook(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

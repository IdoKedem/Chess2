from base import IBasePiece
from board import Square


class Knight(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

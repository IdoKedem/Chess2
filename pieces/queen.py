from base import IBasePiece
from board import Square


class Queen(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

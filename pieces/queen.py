from board import Square
from .base import IBasePiece


class Queen(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

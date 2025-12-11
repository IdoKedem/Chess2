from board import Square
from .base import IBasePiece


class Bishop(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

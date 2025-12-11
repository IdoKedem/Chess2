from board import Square
from .base import IBasePiece


class King(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

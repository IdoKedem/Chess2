from base import IBasePiece
from board import Square


class King(IBasePiece):

    def legal_squares(self) -> set[Square]:
        raise NotImplementedError

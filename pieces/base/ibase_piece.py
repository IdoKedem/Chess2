from abc import ABC

from board import Square
from .color import Color


class IBasePiece(ABC):
    def __init__(self,
                 starting_square: Square,
                 color: Color):
        self.cur_square = starting_square
        self._color = color

        self._legal_squares: set[Square] = set()

    @property
    def color(self) -> Color:
        return self._color

    @property
    def legal_squares(self) -> set[Square]:
        return self._legal_squares

    def update_legal_squares(self) -> None:
        pass

    def __str__(self) -> str:
        return 'BasePiece'

from abc import ABC

from board import Square
from .color import Color


class IBasePiece(ABC):
    def __init__(self,
                 starting_square: Square,
                 color: Color):
        self.cur_square = starting_square
        self._color = color

        self._legal_squares: set[Square]

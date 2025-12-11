from typing import Type

from pieces import IBasePiece


class Player:
    def __init__(self, starting_pieces: dict[Type[IBasePiece], IBasePiece]):
        self.pieces = starting_pieces

    def __str__(self) -> str:
        return '\n'.join([f'{piece_name}: {owned_pieces}'
                          for piece_name, owned_pieces
                          in self.pieces.items()])

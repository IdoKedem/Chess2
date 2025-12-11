from board import Square, Column, Rank
from pieces import King, Color, Pawn


def main() -> None:
    square = Square(rank=Rank.A,
                    column=Column.ONE)

    king = King(square, color=Color.WHITE)
    pawn = Pawn(square, Color.BLACK)
    print(king)
    print(pawn)


if __name__ == '__main__':
    main()

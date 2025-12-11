from pydantic import BaseModel

from .column import Column
from .rank import Rank


class Square(BaseModel):
    rank: Rank
    column: Column

    def __str__(self):
        return f'{self.rank + self.column}'

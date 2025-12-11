from pydantic import BaseModel

from .column import Column
from .rank import Rank


class Square(BaseModel):
    rank: Rank
    column: Column

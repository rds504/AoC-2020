from functools import reduce
from operator import mul
from typing import Iterable

def product(seq: Iterable[int]) -> int:
    return reduce(mul, seq)

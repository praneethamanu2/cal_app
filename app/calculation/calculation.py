from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class Calculation:
    operation: str
    operands: Tuple[float, ...]
    result: float

    def __str__(self) -> str:
        ops = " ".join(str(x) for x in self.operands)
        return f"{self.operation} {ops} = {self.result}"

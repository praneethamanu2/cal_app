from __future__ import annotations
from typing import Callable, Dict, Tuple
from app.calculation.calculation import Calculation
from app.operation import operations as ops

_OPS: Dict[str, Callable[..., float]] = {
    "add": ops.add,
    "subtract": ops.subtract,
    "multiply": ops.multiply,
    "divide": ops.divide,
}

class CalculationFactory:
    @staticmethod
    def create(operation: str, operands: Tuple[float, ...]) -> Calculation:
        op = operation.lower()
        if op not in _OPS:
            raise ValueError(f"Unknown operation: {operation}")
        if len(operands) < 2:
            raise ValueError("At least two operands are required.")
        func = _OPS[op]
        result = func(*operands)
        return Calculation(operation=op, operands=operands, result=result)

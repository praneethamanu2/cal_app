from __future__ import annotations
from functools import reduce

def add(*nums: float) -> float:
    """Sum of numbers."""
    return sum(nums)

def subtract(first: float, *rest: float) -> float:
    """Left-associative subtraction."""
    result = first
    for n in rest:
        result -= n
    return result

def multiply(*nums: float) -> float:
    """Product of numbers."""
    return reduce(lambda a, b: a * b, nums, 1.0)

def divide(first: float, *rest: float) -> float:
    """Left-associative division (EAFP: raises on divide-by-zero)."""
    result = float(first)
    for n in rest:
        result /= n  # ZeroDivisionError if n == 0
    return result

import pytest
from app.operation import operations as ops

@pytest.mark.parametrize("nums, expected", [
    ((1, 2, 3), 6),
    ((-1, 2.5), 1.5),
    ((0,), 0),
])
def test_add(nums, expected):
    assert ops.add(*nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ((10, 3, 2), 5),
    ((-5, -5), 0),
])
def test_subtract(nums, expected):
    assert ops.subtract(*nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ((2, 3, 4), 24),
    ((-1, 2), -2),
    ((2.5, 2), 5.0),
])
def test_multiply(nums, expected):
    assert ops.multiply(*nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ((8, 2, 2), 2),
    ((9, 3), 3),
    ((2.5, 0.5), 5.0),
])
def test_divide(nums, expected):
    assert ops.divide(*nums) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        ops.divide(1, 0)

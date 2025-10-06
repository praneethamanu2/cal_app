import pytest
from app.calculation.factory import CalculationFactory

def test_create_addition_and_str():
    c = CalculationFactory.create("add", (1.0, 2.0))
    assert c.operation == "add"
    assert c.operands == (1.0, 2.0)
    assert c.result == 3.0
    assert str(c) == "add 1.0 2.0 = 3.0"

@pytest.mark.parametrize("op,operands,expected", [
    ("subtract", (5.0, 2.0), 3.0),
    ("multiply", (3.0, 4.0), 12.0),
    ("divide", (9.0, 3.0), 3.0),
])
def test_factory_other_ops(op, operands, expected):
    c = CalculationFactory.create(op, operands)
    assert c.result == expected

def test_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("power", (2.0, 3.0))

def test_operand_count():
    with pytest.raises(ValueError):
        CalculationFactory.create("add", (1.0,))

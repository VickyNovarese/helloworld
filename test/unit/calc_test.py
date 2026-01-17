import pytest
from app.calc import Calculator


def test_divide_by_zero_raises():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.divide(2, 0)

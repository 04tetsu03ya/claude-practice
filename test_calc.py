import pytest
from simple_calc import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5
    assert subtract(-2, -3) == 1
    assert subtract(1.5, 0.5) == 1.0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    assert multiply(1.5, 2) == 3.0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(-9, 3) == -3.0
    assert divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(5, 0)

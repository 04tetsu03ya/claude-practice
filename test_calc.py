import math
import pytest
from simple_calc import add, subtract, multiply, divide, sqrt, power, abs_diff


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


def test_sqrt():
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    assert sqrt(2) == pytest.approx(math.sqrt(2))


def test_sqrt_negative():
    with pytest.raises(ValueError, match="負の数の平方根は計算できません"):
        sqrt(-1)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, -1) == pytest.approx(1 / 3)
    assert power(4, 0.5) == pytest.approx(2.0)


def test_abs_diff():
    assert abs_diff(5, 3) == 2
    assert abs_diff(3, 5) == 2
    assert abs_diff(0, 0) == 0
    assert abs_diff(-3, -7) == 4
    assert abs_diff(-1, 1) == 2
    assert abs_diff(1.5, 3.0) == pytest.approx(1.5)

import math
import pytest
from simple_calc import add, subtract, multiply, divide, sqrt, power, abs_diff, mean, median, mode, standard_deviation, reverse_string, count_vowels, is_palindrome


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


def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3.0
    assert mean([10]) == 10.0
    assert mean([-2, 0, 2]) == 0.0
    assert mean([1.5, 2.5]) == pytest.approx(2.0)


def test_mean_empty():
    with pytest.raises(ValueError, match="データが空です"):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2.0
    assert median([5]) == 5.0
    assert median([7, 3, 1, 5, 9]) == 5.0


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([10, 20]) == 15.0
    assert median([1, 3, 5, 7]) == 4.0


def test_median_empty():
    with pytest.raises(ValueError, match="データが空です"):
        median([])


def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    assert mode([5]) == 5
    assert mode([3, 1, 3, 2, 1, 3]) == 3


def test_mode_tie():
    # 最頻値が複数ある場合は最小値を返す
    assert mode([1, 2, 1, 2]) == 1
    assert mode([3, 4, 3, 4, 5]) == 3


def test_mode_empty():
    with pytest.raises(ValueError, match="データが空です"):
        mode([])


def test_standard_deviation():
    assert standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0)
    assert standard_deviation([0]) == pytest.approx(0.0)
    assert standard_deviation([1, 1, 1]) == pytest.approx(0.0)
    assert standard_deviation([0, 10]) == pytest.approx(5.0)


def test_standard_deviation_empty():
    with pytest.raises(ValueError, match="データが空です"):
        standard_deviation([])


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""
    assert reverse_string("12345") == "54321"


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0
    assert count_vowels("Python") == 1


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("Racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("Was it a car or a cat I saw") is True

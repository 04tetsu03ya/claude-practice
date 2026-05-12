import pytest
from temperature_converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    is_normal_body_temperature,
    calculate_bmi,
    classify_bmi,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0  # 摂氏と華氏が一致する点


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0.0
    assert celsius_to_kelvin(100) == 373.15


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(-40) == -40.0


def test_fahrenheit_to_kelvin():
    assert fahrenheit_to_kelvin(32) == pytest.approx(273.15)
    assert fahrenheit_to_kelvin(212) == pytest.approx(373.15)


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(373.15) == pytest.approx(100.0)
    assert kelvin_to_celsius(0) == -273.15


def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == pytest.approx(32.0)
    assert kelvin_to_fahrenheit(373.15) == pytest.approx(212.0)


def test_celsius_below_absolute_zero():
    with pytest.raises(ValueError, match="絶対零度"):
        celsius_to_fahrenheit(-300)
    with pytest.raises(ValueError, match="絶対零度"):
        celsius_to_kelvin(-300)


def test_fahrenheit_below_absolute_zero():
    with pytest.raises(ValueError, match="絶対零度"):
        fahrenheit_to_celsius(-500)


def test_kelvin_below_zero():
    with pytest.raises(ValueError, match="ケルビンは0未満"):
        kelvin_to_celsius(-1)
    with pytest.raises(ValueError, match="ケルビンは0未満"):
        kelvin_to_fahrenheit(-1)


def test_is_normal_body_temperature():
    assert is_normal_body_temperature(35.9) == "低体温"
    assert is_normal_body_temperature(36.0) == "正常"
    assert is_normal_body_temperature(36.5) == "正常"
    assert is_normal_body_temperature(37.4) == "正常"
    assert is_normal_body_temperature(37.5) == "微熱"
    assert is_normal_body_temperature(38.4) == "微熱"
    assert is_normal_body_temperature(38.5) == "発熱"
    assert is_normal_body_temperature(40.0) == "発熱"


def test_is_normal_body_temperature_below_absolute_zero():
    with pytest.raises(ValueError, match="絶対零度"):
        is_normal_body_temperature(-300)


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.857, rel=1e-3)
    assert calculate_bmi(50, 1.60) == pytest.approx(19.531, rel=1e-3)
    assert calculate_bmi(90, 1.70) == pytest.approx(31.141, rel=1e-3)


def test_calculate_bmi_invalid():
    with pytest.raises(ValueError, match="体重"):
        calculate_bmi(0, 1.75)
    with pytest.raises(ValueError, match="体重"):
        calculate_bmi(-10, 1.75)
    with pytest.raises(ValueError, match="身長"):
        calculate_bmi(70, 0)
    with pytest.raises(ValueError, match="身長"):
        calculate_bmi(70, -1.75)


def test_classify_bmi():
    assert classify_bmi(16.0) == "低体重"
    assert classify_bmi(18.4) == "低体重"
    assert classify_bmi(18.5) == "普通体重"
    assert classify_bmi(22.0) == "普通体重"
    assert classify_bmi(24.9) == "普通体重"
    assert classify_bmi(25.0) == "過体重"
    assert classify_bmi(27.5) == "過体重"
    assert classify_bmi(29.9) == "過体重"
    assert classify_bmi(30.0) == "肥満"
    assert classify_bmi(35.0) == "肥満"


def test_classify_bmi_invalid():
    with pytest.raises(ValueError, match="BMI"):
        classify_bmi(0)
    with pytest.raises(ValueError, match="BMI"):
        classify_bmi(-5)

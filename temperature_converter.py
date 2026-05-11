def celsius_to_fahrenheit(c):
    """摂氏を華氏に変換する。"""
    if c < -273.15:
        raise ValueError("絶対零度（-273.15°C）未満の温度は存在しません")
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    """摂氏をケルビンに変換する。"""
    if c < -273.15:
        raise ValueError("絶対零度（-273.15°C）未満の温度は存在しません")
    return c + 273.15


def fahrenheit_to_celsius(f):
    """華氏を摂氏に変換する。"""
    if f < -459.67:
        raise ValueError("絶対零度（-459.67°F）未満の温度は存在しません")
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    """華氏をケルビンに変換する。"""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_celsius(k):
    """ケルビンを摂氏に変換する。"""
    if k < 0:
        raise ValueError("ケルビンは0未満になりません")
    return k - 273.15


def kelvin_to_fahrenheit(k):
    """ケルビンを華氏に変換する。"""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

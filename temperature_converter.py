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


def calculate_bmi(weight_kg, height_m):
    """体重（kg）と身長（m）からBMIを計算する。

    Raises:
        ValueError: 体重または身長が0以下の場合
    """
    if weight_kg <= 0:
        raise ValueError("体重は0より大きい値を指定してください")
    if height_m <= 0:
        raise ValueError("身長は0より大きい値を指定してください")
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """BMI値から体格を分類する（WHO基準）。

    Returns:
        str: "低体重" / "普通体重" / "過体重" / "肥満"

    Raises:
        ValueError: BMIが0以下の場合
    """
    if bmi <= 0:
        raise ValueError("BMIは0より大きい値を指定してください")
    if bmi < 18.5:
        return "低体重"
    elif bmi < 25.0:
        return "普通体重"
    elif bmi < 30.0:
        return "過体重"
    else:
        return "肥満"


def is_normal_body_temperature(celsius):
    """体温が正常範囲（36.0〜37.4°C）かどうかを判定する。

    Returns:
        str: "低体温" / "正常" / "微熱" / "発熱"
    """
    if celsius < -273.15:
        raise ValueError("絶対零度（-273.15°C）未満の温度は存在しません")
    if celsius < 36.0:
        return "低体温"
    elif celsius <= 37.4:
        return "正常"
    elif celsius <= 38.4:
        return "微熱"
    else:
        return "発熱"

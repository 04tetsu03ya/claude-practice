# claude-practice

Python の学習・練習用リポジトリ。計算機モジュールと温度変換モジュールを含む。

---

## simple_calc.py

四則演算・平方根・べき乗・差の絶対値を提供する純粋関数モジュール。
対話型 CLI としても起動できる。

### 関数一覧

| 関数 | 説明 |
|---|---|
| `add(a, b)` | 和を返す |
| `subtract(a, b)` | 差を返す |
| `multiply(a, b)` | 積を返す |
| `divide(a, b)` | 商を返す。`b=0` のとき `ValueError` |
| `sqrt(a)` | 平方根を返す。`a<0` のとき `ValueError` |
| `power(a, b)` | `a` の `b` 乗を返す |
| `abs_diff(a, b)` | 差の絶対値を返す |

### 使用例

```python
from simple_calc import add, divide, sqrt

add(3, 5)       # => 8
divide(10, 4)   # => 2.5
sqrt(9)         # => 3.0
```

### エラー仕様

```python
divide(5, 0)   # ValueError: 0で割ることはできません
sqrt(-1)       # ValueError: 負の数の平方根は計算できません
```

### 対話型 CLI

```bash
python simple_calc.py
```

---

## temperature_converter.py

摂氏・華氏・ケルビン間の相互変換と体温判定を提供するモジュール。

### 関数一覧

| 関数 | 説明 |
|---|---|
| `celsius_to_fahrenheit(c)` | 摂氏 → 華氏 |
| `celsius_to_kelvin(c)` | 摂氏 → ケルビン |
| `fahrenheit_to_celsius(f)` | 華氏 → 摂氏 |
| `fahrenheit_to_kelvin(f)` | 華氏 → ケルビン |
| `kelvin_to_celsius(k)` | ケルビン → 摂氏 |
| `kelvin_to_fahrenheit(k)` | ケルビン → 華氏 |
| `is_normal_body_temperature(celsius)` | 体温判定（低体温/正常/微熱/発熱） |

### 使用例

```python
from temperature_converter import celsius_to_fahrenheit, is_normal_body_temperature

celsius_to_fahrenheit(100)           # => 212.0
is_normal_body_temperature(36.5)     # => "正常"
is_normal_body_temperature(38.5)     # => "発熱"
```

### 体温判定の基準

| 戻り値 | 範囲 |
|---|---|
| 低体温 | 36.0°C 未満 |
| 正常 | 36.0°C 〜 37.4°C |
| 微熱 | 37.5°C 〜 38.4°C |
| 発熱 | 38.5°C 以上 |

### エラー仕様

絶対零度未満（-273.15°C 以下）を渡すと `ValueError` が発生する。

---

## テストの実行

```bash
# 全テストを実行
python -m pytest -v

# 計算機のテストのみ
python -m pytest test_calc.py -v

# 温度変換のテストのみ
python -m pytest test_temperature_converter.py -v
```

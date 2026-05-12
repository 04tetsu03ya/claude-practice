import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def sqrt(a):
    """平方根を計算する。"""
    if a < 0:
        raise ValueError("負の数の平方根は計算できません")
    return math.sqrt(a)


def power(a, b):
    """aのb乗を計算する。"""
    return a ** b


def abs_diff(a, b):
    """2つの数の差の絶対値を返す。"""
    return abs(a - b)


def mean(data):
    """データの平均値を計算する。"""
    if not data:
        raise ValueError("データが空です")
    return sum(data) / len(data)


def median(data):
    """データの中央値を計算する。"""
    if not data:
        raise ValueError("データが空です")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return float(sorted_data[mid])


def mode(data):
    """データの最頻値を計算する。最頻値が複数ある場合は最小値を返す。"""
    if not data:
        raise ValueError("データが空です")
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    return min(k for k, v in counts.items() if v == max_count)


def standard_deviation(data):
    """データの母標準偏差を計算する。"""
    if not data:
        raise ValueError("データが空です")
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def main():
    print("=== 簡単な計算機 ===")
    print("演算子: + - * /")
    print("終了するには 'q' を入力してください")
    print()

    while True:
        expr = input("計算式を入力 (例: 3 + 5): ").strip()
        if expr.lower() == "q":
            break

        parts = expr.split()
        if len(parts) != 3:
            print("形式が正しくありません。例: 3 + 5")
            continue

        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
        except ValueError:
            print("数値が正しくありません")
            continue

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print(f"未対応の演算子: {op}")
                continue

            print(f"結果: {result}")
        except ValueError as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()

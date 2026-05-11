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

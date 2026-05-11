# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# テストを全件実行
python -m pytest test_calc.py -v

# 特定のテスト関数を実行
python -m pytest test_calc.py::test_divide -v

# 計算機をインタラクティブに起動
python simple_calc.py
```

## Architecture

このリポジトリは2層構造になっている。

- **`simple_calc.py`** — ロジック層。`add` / `subtract` / `multiply` / `divide` の4関数と、対話型CLIの `main` 関数を含む。ロジック関数は副作用なしの純粋関数として独立しており、`main` からも `test_calc.py` からも直接インポートして使う。
- **`test_calc.py`** — テスト層。pytest を使い、上記4関数を直接インポートしてテストする。`main` はテスト対象外。

`divide` はゼロ除算時に `ValueError` を送出する（`ZeroDivisionError` ではない）点に注意。

## Coding Conventions

- コメントは日本語で書く
- 関数には必ず docstring を書く
- エラーメッセージは日本語にする

# Hexorcist — Base Converter

A simple program that converts numbers between any two bases (2–36) **without using built-in Python base conversion**. Perfect for learning how numbers really work!

## How It Works

- **Step 1:** Convert the input number to decimal using a "decoder ring" (0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ).
- **Step 2:** Convert the decimal number to the target base using division and remainders.

## Usage

1. Run the program: `python hexorcist.py`
2. Enter the number to convert, its current base, and the target base.
3. The program will display the converted number.

## Rules

No `bin()`, `hex()`, `oct()`, `format()`, or `int(..., base)` allowed. Only loops, math, and your own brain!

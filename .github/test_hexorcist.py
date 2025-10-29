# test_hexorcist.py
from hexorcist import to_decimal, from_decimal

def test_to_decimal():
    assert to_decimal("C7", 16) == 199
    assert to_decimal("1010", 2) == 10
    assert to_decimal("1A4", 16) == 420

def test_from_decimal():
    assert from_decimal(199, 16) == "C7"
    assert from_decimal(10, 2) == "1010"
    assert from_decimal(420, 16) == "1A4"

import pytest
from testing_calculator.calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(2, 3) == 5

#python -m pytest test_calculator.py -v

def test_sb():
    assert subtract(3, 2) == 1
    assert subtract(-3, 2) == -5

def test_mtp():
    assert multiply(2, 3) == 6
    assert multiply(-2 ,3) == -6

def test_div():
    assert divide(6, 2) == 3
    assert divide(6, 0) == "Errror: Division by zero"
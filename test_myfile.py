import pytest
from myfile import Calculus_Calculator
import math

def test_all_pass():
    assert Calculus_Calculator.logarithm(1000) == pytest.approx(3, rel=1e-5)
    assert Calculus_Calculator.power(5, 2) == 25
    assert Calculus_Calculator.fact(5) == 120

def test_all_fail():
    assert Calculus_Calculator.logarithm(1000) == 5
    assert Calculus_Calculator.power(5, 2) == 20
    assert Calculus_Calculator.fact(5) == 130
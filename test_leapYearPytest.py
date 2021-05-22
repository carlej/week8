import pytest
import lpYear

def test_gd():
    assert lpYear.leapYear(2020) == True
def test_bd():
    assert lpYear.leapYear(2021) == False

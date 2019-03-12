import pytest
from app import fibR
from app import is_prime
def test_fib_1_equals_1():
    assert fibR(1) == 1

def test_fib_2_equals_1():
    assert fibR(2) == 1

def test_fib_6_equals_8():
    assert fibR(6) == 8

def test_is_prime_6_equals_6():
    assert is_prime(6) == False

def test_is_prime_7_equals_7():
    assert is_prime(7) == True

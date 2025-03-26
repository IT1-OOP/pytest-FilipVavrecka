import pytest
from src import calculator

def test_add(a, b):
    assert calculator.add(5, 3) == 8
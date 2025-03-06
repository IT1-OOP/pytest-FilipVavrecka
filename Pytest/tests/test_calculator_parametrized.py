import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0,0) == 0

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

def test_add_wrong():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(5,-8) == -3

    @pytest.mark.parametrize(
        "x,y,expected",
            [
                (1,2,3),
                (0,5,5), 
                (-2,9,7), 
                (5,-8,-3),
            ],
        )
    def test_add_parametrized(x,y,expected):
        assert calculator.add(x,y) == expected

def test_subtract():
    assert calculator.subtract(5,3) == 2
    assert calculator.subtract(0,5) == -5
    assert calculator.subtract(-2,9) == -11
    assert calculator.subtract(5,-8) == 13

    @pytest.mark.parametrize(
        "a,b,expected",
            [
                (5,3,2),
                (0,5,-5), 
                (-2,9,-11), 
                (5,-8,13),
            ],
        )
    def test_subtract_parametrized(a,b,expected):
        assert calculator.subtract(a,b) == expected

def test_subtract_wrong():
    assert calculator.subtract(5,3) == 3
    assert calculator.subtract(0,5) == -6
    assert calculator.subtract(-2,9) == -12
    assert calculator.subtract(5,-8) == 15

    @pytest.mark.parametrize(
        "a,b,expected",
            [
                (5,3,3),
                (0,5,-6), 
                (-2,9,-12), 
                (5,-8,15),
            ],
        )
    def test_subtract_parametrized(a,b,expected):
        assert calculator.subtract(a,b) == expected

def test_multiply():
    assert calculator.multiply(5,3) == 15
    assert calculator.multiply(0,5) == 0
    assert calculator.multiply(-2,9) == -18
    assert calculator.multiply(5,-8) == -40

    @pytest.mark.parametrize(
        "a,b,expected",
            [
                (5,3,15),
                (0,5,0), 
                (-2,9,-18), 
                (5,-8,-40),
            ],
        )
    def test_multiply_parametrized(a,b,expected):
        assert calculator.multiply(a,b) == expected

def test_multiply_wrong():
    assert calculator.multiply(5,3) == 18
    assert calculator.multiply(0,5) == 4
    assert calculator.multiply(-2,9) == -20
    assert calculator.multiply(5,-8) == -50

    @pytest.mark.parametrize(
        "a,b,expected",
            [
                (5,3,18),
                (0,5,4), 
                (-2,9,-20), 
                (5,-8,-50),
            ],
        )
    def test_multiply_parametrized(a,b,expected):
        assert calculator.multiply(a,b) == expected

import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5,-8) == -3

    @pytest.mark.parametrize(
        "a,b,expected",
            [
                (1,2,3),
                (0,5,5), 
                (-2,9,7), 
                (5,-8,-3),
            ],
        )
    def test_add_parametrized(a,b,expected):
        assert calculator.add(a,b) == expected
    

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

@pytest.mark.parametrize(
    "a, b, expected_exception, expected_message",
    [
        (0, 5, ValueError, "Cannot take log of non-positive number!"),
        (-2, 5, ValueError, "Cannot take log of non-positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)

def test_log(a, b, expected_exception, expected_message):
    with pytest.raises(expected_exception) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_message
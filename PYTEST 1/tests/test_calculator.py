import pytest
import math
from src.quadratic import solve_quadratic_formula
from src import calculator

def test_add(a, b):
    assert calculator.add(5, 3) == 8

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -3, 2, (2.0, 1.0)),
        (1, 2, 1, (-1.0, -1.0)),
        (2, 5, -3, (0.5, -3.0)),
    ],
)

def test_solve_quadratic_valid(a, b, c, expected):
    assert solve_quadratic_formula(a, b, c) == expected


def test_solve_quadratic_exceptions():
    with pytest.raises(TypeError):
        solve_quadratic_formula("a", 2, 3)
    with pytest.raises(TypeError):
        solve_quadratic_formula(1, [2], 3)
    with pytest.raises(TypeError):
        solve_quadratic_formula(1, 2, None)
    with pytest.raises(SyntaxError):
        solve_quadratic_formula(0, 2, 3)
    with pytest.raises(NameError):
        solve_quadratic_formula(1, 5, 3)
    with pytest.raises(ValueError):
        solve_quadratic_formula(1, 2, 5)

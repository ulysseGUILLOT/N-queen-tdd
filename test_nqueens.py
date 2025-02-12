import pytest
from nqueens import *

def test_nqueens_1():
    result = solve_nqueens(1)
    expected = [[1]]
    assert result == expected


@pytest.mark.parametrize("n, expected", [
    (1, [[0]]),

    (2, [[0, 0],
         [0, 0]]),

    (3, [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]),

    (4, [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]])
])
def test_create_board(n, expected):
    assert create_board(n) == expected
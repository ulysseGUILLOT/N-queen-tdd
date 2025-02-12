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


def test_is_safe():
    board = create_board(4)

    # place une reine en 0:0
    board[0][0] = 1

    assert is_safe(board, 0, 0, 4) == False
    assert is_safe(board, 1, 0, 4) == True
    assert is_safe(board, 2, 0, 4) == True
    assert is_safe(board, 0, 2, 4) == False
    assert is_safe(board, 0, 3, 4) == False
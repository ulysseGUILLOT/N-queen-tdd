import pytest
from nqueens import solve_nqueens

def test_nqueens_1():
    result = solve_nqueens(1)
    expected = [["#"]]
    assert result == expected
import pytest
from main import Solution


def test_solution_1():
    sol = Solution()
    x = [7, 1, 5, 3, 6, 4]
    result = sol.max_profit(x)
    assert result == 7


def test_solution_2():
    sol = Solution()
    x = [1, 2, 3, 4, 5]
    result = sol.max_profit(x)
    assert result == 4


def test_solution_3():
    sol = Solution()
    x = [7, 6, 4, 3, 1]
    result = sol.max_profit(x)
    assert result == 0

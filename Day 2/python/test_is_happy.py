import pytest
from main import Solution


def test_solution_1():
    sol = Solution()
    x = 1
    result = sol.is_happy(x)
    assert result == 1


def test_solution_2():
    sol = Solution()
    x = 2
    result = sol.is_happy(x)
    assert result == 0


def test_solution_3():
    sol = Solution()
    x = 2
    result = sol.is_happy(x)
    assert result == 0


def test_solution_4():
    sol = Solution()
    x = 2
    result = sol.is_happy(x)
    assert result == 0
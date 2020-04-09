import pytest
from main import Solution


def test_solution_1():
    sol = Solution()
    x = [1, 2, 3]
    result = sol.count_elements(x)
    assert result == 2


def test_solution_2():
    sol = Solution()
    x = [1, 1, 3, 3, 5, 5, 7, 7]
    result = sol.count_elements(x)
    assert result == 0


def test_solution_3():
    sol = Solution()
    x = [1, 3, 2, 3, 5, 0]
    result = sol.count_elements(x)
    assert result == 3


def test_solution_4():
    sol = Solution()
    x = [1, 1, 2, 2]
    result = sol.count_elements(x)
    assert result == 2

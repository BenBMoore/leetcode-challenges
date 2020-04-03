import pytest
from main import Solution


def test_solution_no_sum_solution():
    sol = Solution()
    x = [2, 1, -14, 10, -9, 5, -12]
    result = sol.max_sub_array(x)
    assert result == 10


def test_solution_sum_solution():
    sol = Solution()
    x = [-4, 3, 4, -7, 1, 6, ]
    result = sol.max_sub_array(x)
    assert result == 7


def test_solution_all_neg():
    sol = Solution()
    x = [-4, -3, -4, -7, -1, -6]
    result = sol.max_sub_array(x)
    assert result == -1


def test_solution_all_positive():
    sol = Solution()
    x = [1, 2, 3, 4, 5, 6]
    result = sol.max_sub_array(x)
    assert result == 21

import pytest
from main import Solution


def test_solution_all_zeroes():
    sol = Solution()
    x = [0, 0, 0, 0, 0]
    sol.move_zeroes(x)
    assert x == [0, 0, 0, 0, 0]


def test_solution_no_zeroes():
    sol = Solution()
    x = [3, 2, 5, 3, 3]
    sol.move_zeroes(x)
    assert x == [3, 2, 5, 3, 3]

def test_solution_leading_zeroes():
    sol = Solution()
    x = [0, 0, 3, 2, 1]
    sol.move_zeroes(x)
    assert x == [3, 2, 1, 0, 0]


def test_solution_ending_zeroes():
    sol = Solution()
    x = [5, 15, 6, 0, 0]
    sol.move_zeroes(x)
    assert x == [5, 15, 6, 0, 0]


def test_solution_leading_middle_ending_zeroes():
    sol = Solution()
    x = [0, 3, 4, 0, 0, 2, 5, 19, 0]
    sol.move_zeroes(x)
    assert x == [3, 4, 2, 5, 19, 0, 0, 0, 0]
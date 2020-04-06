import pytest
from main import Solution


def test_solution_1():
    sol = Solution()
    x = ["abc", "bca", "cba"]
    result = sol.group_anagrams(x)
    assert result == [["abc", "bca", "cba"]]


def test_solution_2():
    sol = Solution()
    x = ["abc", "bca", "cba", "better", "retteb"]
    result = sol.group_anagrams(x)
    assert result == [["abc", "bca", "cba"], ["better", "retteb"]]


def test_solution_1():
    sol = Solution()
    x = ["eads", "asdsadsa", "aresdfsd"]
    result = sol.group_anagrams(x)
    assert result == [["eads"], ["asdsadsa"], ["aresdfsd"]]

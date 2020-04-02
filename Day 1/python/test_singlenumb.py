import pytest
from main import Solution
    

def test_solutions_1():
    sol = Solution()
    x = [1,3,2,4,2,3,4]
    result = sol.singleNumber(x)
    assert result == 1


def test_solutions_2():
    sol = Solution()
    x = [9, 323232,1233,323232,1233]
    result = sol.singleNumber(x)
    assert result == 9
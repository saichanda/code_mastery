import pytest

class Solution:
    def isHappy(self, n):
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1: return True
        return False
    
    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n //= 10
        return output

@pytest.mark.parametrize("n, expected", [(19, True), (2, False), (7, True)])
def test_is_happy(n, expected):
    assert Solution().isHappy(n) == expected

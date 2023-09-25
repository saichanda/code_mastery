"""
    Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits 
    and whose sum of digits should be equals to 'S'.
"""

import pytest
import numpy as np


class Solution:
    def findLargest(self, N, S, sol):
        ans = ""
        total = 0
        tmp = S
        if S == 0 and N > 1:
            return -1
        for _ in range(N):
            if S >= 9:
                S = S - 9
                ans += "9"
                total += 9
            else:
                ans += str(S)
                total += S
                break
        if len(ans) < N:
            for _ in range(N - len(ans)):
                ans += "0"

        np.testing.assert_allclose([int(ans)], [sol])


@pytest.mark.parametrize(
    "N, S, sol",
    (
        (
            2,
            9,
            90,
        ),
    ),
)
def test_largest_number(N, S, sol):
    Solution().findLargest(N, S, sol)

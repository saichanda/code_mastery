#Date:31-01-26
import pytest
import numpy as np

class Solution:
    def missingNumber(self, arr, n, sol):
        total = n * (n + 1) // 2
        curr = sum(arr)
        res = total - curr
        np.testing.assert_allclose(res, sol)


@pytest.mark.parametrize(
    "N, arr, sol",
    [
        (5, [1, 2, 3, 5], 4),
        (3, [1, 3], 2),
    ],
)
def test_missing_number(N, arr, sol):
    Solution().missingNumber(arr, N, sol)
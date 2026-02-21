"""
30/01/2026
Given an array of integers, count how many elements are even.
"""

import pytest
import numpy as np

class Solution:
    def countEvens(self, arr, sol):
        count = 0
        for num in arr:
            if num % 2 == 0:
                count += 1

        np.testing.assert_equal(count, sol)


@pytest.mark.parametrize(
    "arr, sol",
    [
        ([1, 2, 3, 4, 6], 3),
        ([1, 3, 5], 0),
    ]
)
def test_countEvens(arr, sol):
    Solution().countEvens(arr, sol)


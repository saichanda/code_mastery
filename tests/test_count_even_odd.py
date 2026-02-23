"""
Date:31/01/2026
Python
Given an array of integers, count how many elements are even and odd.
"""

import pytest
import numpy as np


class Solution:
    def countEvenOdd(self, arr, even_sol, odd_sol):
        even_count = 0
        odd_count = 0

        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        np.testing.assert_equal(even_count, even_sol)
        np.testing.assert_equal(odd_count, odd_sol)


@pytest.mark.parametrize(
    "arr, even_sol, odd_sol",
    [
        ([1, 2, 3, 4, 6], 3, 2),
        ([1, 3, 5], 0, 3),
        ([2, 4, 6], 3, 0),
    ]
)
def test_countEvenOdd(arr, even_sol, odd_sol):
    Solution().countEvenOdd(arr, even_sol, odd_sol)
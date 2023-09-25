"""
    Given a sorted array arr containing n elements with possibly duplicate
    is to find indexes of first elements, the task is to find the first and
    last occurrences of an element x in the given array.

    Returns:
        int: first index of the element x
        int: last index of the element x
"""

import pytest
import numpy as np


class Solution:
    def find(self, arr, n, x, sol):
        if x not in arr:
            return -1, -1
        first = 0
        last = n - 1
        for _ in range(n):
            if arr[first] == x and arr[last] == x:
                break
            if arr[first] != x:
                first += 1
            if arr[last] != x:
                last -= 1
        res = [first, last]
        np.testing.assert_allclose(res, sol)


@pytest.mark.parametrize(
    "N, arr, x, sol",
    (
        (
            5,
            [2, 3, 1, 2, 3],
            3,
            [1, 4],
        ),
    ),
)
def test_first_last_x(N, arr, x, sol):
    Solution().find(arr, N, x, sol)

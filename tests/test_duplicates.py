"""
    Given an array a of size N which contains elements from 0 to N-1, 
    you need to find all the elements occurring more than once in the given array. 
    Return the answer in ascending order. If no such element is found, return list containing [-1]. 

    Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 
"""

import pytest
import numpy as np


class Solution:
    def duplicates(self, arr, n, sol):
        for i in range(n):
            idx = arr[i] % n
            arr[idx] += n
        res = [i for i in range(n) if arr[i] // n >= 2]
        np.testing.assert_allclose(res, sol)


@pytest.mark.parametrize(
    "N, arr, sol",
    ((5, [2, 3, 1, 2, 3], [2, 3]),),
)
def test_duplicates(N, arr, sol):
    Solution().duplicates(arr, N, sol)

"""
    Problem Statement:
    Lucky numbers are subset of integers.
    Take the set of integers
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,……
    First, delete every second number, we get following reduced set.
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19,…………
    Now, delete every third number, we get
    1, 3, 7, 9, 13, 15, 19,….….
    Continue this process indefinitely……
    Any number that does NOT get deleted due to above process is called “lucky”.

You are given a number N, you need to tell whether the number is lucky or not.
"""

import pytest
import numpy as np


class Solution:
    def isLucky(self, n, sol):
        arr = list(range(1, n + 1))
        index = 0
        j = 1
        flag = 0
        while True:
            while index + j < len(arr):
                arr[index + j] = 0
                index += j + 1
            while 0 in arr:
                arr.remove(0)
            j += 1
            index = 0
            if j > len(arr):
                break
        flag = 1 if n in arr else 0
        np.testing.assert_allclose(flag, sol)


# Alternate Solution (Optimized)
class AlternateSolution:
    def isLucky(self, n, sol):
        count = 2
        flag = 0
        while True:
            if n % count == 0:
                flag = 0
                break
            if int(n / count) == 0:
                flag = 1
                break
            n = n - int(n / count)
            count += 1
        np.testing.assert_allclose(flag, sol)


@pytest.mark.parametrize(
    "n, sol",
    (
        (
            19,
            1,
        ),
    ),
)
def test_is_lucky_number_1(n, sol):
    Solution().isLucky(n, sol)


@pytest.mark.parametrize(
    "n, sol",
    (
        (
            19,
            1,
        ),
    ),
)
def test_is_lucky_number_2(n, sol):
    AlternateSolution().isLucky(n, sol)

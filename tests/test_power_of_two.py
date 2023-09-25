"""
    Given a non-negative integer N.
    The task is to check if N is a power of 2.
    More formally, check if N can be expressed as 2^x for some integer x.
"""

import pytest
import numpy as np


class Solution:
    def is_power_of_two(self, n, sol):
        isPower = 0
        flag = True
        if n == 0:
            isPower = 0
        elif n == 1:
            isPower = 1
        while n > 1:
            if n == 2:
                isPower = 1
                break
            if n % 2 == 0:
                n = n / 2
                continue
            else:
                flag = False
                break
        isPower = 0 if not flag or n == 1 else 1
        np.testing.assert_allclose(isPower, sol)


@pytest.mark.parametrize(
    "n, sol",
    (
        (
            1024,
            1,
        ),
    ),
)
def test_power_of_two(n, sol):
    Solution().is_power_of_two(n, sol)

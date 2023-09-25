"""
    Given an integer N and an integer D, rotate the binary representation
    of the integer N by D digits to the left as well as right and 
    return the results in their decimal representation after each of the rotation.
    Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000000000001100.
"""

import pytest
import numpy as np


class Solution:
    def rotate(self, N, D, sol):
        ar = [0] * 16
        if D > 16:
            D = D % 16
        i = len(ar) - 1
        while i >= 0:
            ar[i] = 1 if N % 2 != 0 else 0
            i -= 1
            N = int(N / 2)
            if not N:
                break
        res1 = sum(
            2 ** (len(ar) - i - 1) * ele for i, ele in enumerate(ar[D:] + ar[:D])
        )
        res2 = sum(
            2 ** (len(ar) - i - 1) * ele for i, ele in enumerate(ar[-D:] + ar[:-D])
        )
        res = [res1, res2]
        np.testing.assert_allclose(res, sol)


@pytest.mark.parametrize(
    "N, D, sol",
    ((13, 4, [208, 53248]),),
)
def test_rotate_bits(N, D, sol):
    Solution().rotate(N, D, sol)

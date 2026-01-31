import pytest
import numpy as np

class Solution:
    def moveZeros(self, arr, sol):
        idx = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[idx], arr[i] = arr[i], arr[idx]
                idx += 1
        np.testing.assert_allclose(arr, sol)


@pytest.mark.parametrize(
    "arr, sol",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ]
)
def test_move_zeros(arr, sol):
    Solution().moveZeros(arr, sol)

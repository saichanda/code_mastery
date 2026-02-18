import pytest
import numpy as np


class Solution:
    def findMaxConsecutiveOnes(self, nums, expected):
        max_ones = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
                max_ones = max(max_ones, count)
            else:
                count = 0

        # Assertion for testing
        np.testing.assert_equal(max_ones, expected)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
    ]
)
def test_find_max_consecutive_ones(nums, expected):
    Solution().findMaxConsecutiveOnes(nums, expected)
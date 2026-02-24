"""
Get the maximum element from given array
"""

import pytest

class Solution:
    def get_max(self, arr, expected):
        result = max(arr)
        assert result == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 3, 2, 5, 4], 5),
        ([10, 7, 8], 10),
    ]
)
def test_get_max(arr, expected):
    Solution().get_max(arr, expected)

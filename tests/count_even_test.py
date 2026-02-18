# Date: 18-02-26
import pytest

class Solution:
    def count_evens(self, arr, expected):
        result = sum(1 for x in arr if x % 2 == 0)
        assert result == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 6], 3),
        ([1, 3, 5], 0),
    ]
)
def test_count_evens(arr, expected):
    Solution().count_evens(arr, expected)

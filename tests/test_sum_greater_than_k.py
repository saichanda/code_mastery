import pytest

class Solution:
    def sum_greater_than_k(self, arr, k, expected):
        result = sum(x for x in arr if x > k)
        assert result == expected


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 5, 10, 3], 4, 15),
        ([2, 4, 6], 5, 6),
    ]
)
def test_sum_greater_than_k(arr, k, expected):
    Solution().sum_greater_than_k(arr, k, expected)

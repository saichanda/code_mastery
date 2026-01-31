# Date: 31-01-2026
import pytest

class Solution:
    def is_prime(self, n, expected):
        if n < 2:
            result = False
        else:
            result = all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        assert result == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, True),
        (10, False),
        (1, False),
    ]
)
def test_is_prime(n, expected):
    Solution().is_prime(n, expected)

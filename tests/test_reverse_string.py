import pytest

class Solution:
    def reverse_string(self, s, expected):
        result = s[::-1]
        assert result == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", "olleh"),
        ("pytest", "tsetyp"),
    ]
)
def test_reverse_string(s, expected):
    Solution().reverse_string(s, expected)

# 31-01-2026 Behera is a Hero
import pytest


class Solution:
    def nextGreatestLetter(self, letters, target):
        i, j = 0, len(letters) - 1

        # wrap-around case
        if letters[j] <= target:
            return letters[0]

        # binary search
        while i < j:
            mid = i + (j - i) // 2
            if letters[mid] > target:
                j = mid
            else:
                i = mid + 1

        return letters[i]


@pytest.mark.parametrize(
    "letters, target, expected",
    [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["c", "f", "j"], "d", "f"),
        (["c", "f", "j"], "g", "j"),
        (["c", "f", "j"], "j", "c"),  # wrap-around
    ]
)
def test_next_greatest_letter(letters, target, expected):
    result = Solution().nextGreatestLetter(letters, target)
    assert result == expected

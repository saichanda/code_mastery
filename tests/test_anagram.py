"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.
"""
#Date - 31 - 01 -2026
import pytest

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("aacc", "ccac", False),
    ]
)
def test_anagram(s, t, expected):
    sol = Solution()
    assert sol.is_anagram(s, t) == expected
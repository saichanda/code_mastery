"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in s.
"""

import sys
import pytest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list = list(pattern)
        s_list = s.split(" ")

        if len(p_list) != len(s_list):
            return False

        match = {}

        for i in range(len(p_list)):
            if p_list[i] not in match:
                if s_list[i] in match.values():
                    return False
                match[p_list[i]] = s_list[i]
            elif match[p_list[i]] != s_list[i]:
                return False

        return True


def main():
    """
    Allows manual testing from command line.
    Example:
        python word_pattern.py abba "dog cat cat dog"
    """
    if len(sys.argv) != 3:
        print("Usage: python word_pattern.py <pattern> <string>")
        sys.exit(1)

    pattern = sys.argv[1]
    s = sys.argv[2]

    sol = Solution()
    result = sol.wordPattern(pattern, s)
    print(result)


# ----------------------
# Pytest Test Cases (Parameterized)
# ----------------------

@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
    ],
)
def test_word_pattern(pattern, s, expected):
    sol = Solution()
    assert sol.wordPattern(pattern, s) == expected


if __name__ == "__main__":
    main()

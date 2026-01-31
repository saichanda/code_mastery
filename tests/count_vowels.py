#Dt:- 7/01/2026
# test_count_vowels.py
import pytest

def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0
    assert count_vowels("bcdf") == 0
import pytest

class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n  # XORing a number with itself results in 0
        return res

@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_single_number(nums, expected):
    assert Solution().singleNumber(nums) == expected
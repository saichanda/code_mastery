import pytest

class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        def count_set_bits(n):
            return bin(n).count('1')

        total_sum = 0
        for i in range(len(nums)):
            if count_set_bits(i) == k:
                total_sum += nums[i]
        return total_sum

@pytest.mark.parametrize("nums, k, expected", [
    ([5, 10, 1, 5, 2], 1, 13),
    ([4, 3, 2, 1], 2, 1)
])
def test_sum_indices_with_k_set_bits(nums, k, expected):
    assert Solution().sumIndicesWithKSetBits(nums, k) == expected

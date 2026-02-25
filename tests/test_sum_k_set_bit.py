"""
    You are given a 0-indexed integer array nums and an integer k.

    Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
"""
import pytest

class Solution:
    def binary(self, idx):
        count = 0
        while idx > 0:
            if idx % 2 == 0:
                idx = int(idx/2)
                continue
            else:
                count += 1
                idx = int(idx/2)
        return count
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        sum_k = 0
        for i in range(len(nums)):
            if self.binary(i) == k:
                sum_k += nums[i]
        return sum_k


# --------------------
# Pytest Test Cases
# --------------------

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([5, 10, 1, 5, 2], 1, 13),      # indices with 1 set bit: 1,2,4 → 10+1+2=13
        ([4, 3, 2, 1], 2, 1),           # index 3 has two set bits → nums[3]=1
        ([1, 2, 3, 4, 5, 6], 0, 1),     # only index 0 → nums[0]=1
        ([7, 8, 9, 10], 3, 0),         # index 3 (binary 11 has 2 bits) → actually none → 0
        ([7, 8, 9, 10, 11, 12, 13, 14], 2, 9 + 12 + 14),  # indices 3,5,6
    ],
)
def test_sumIndicesWithKSetBits(nums, k, expected):
    sol = Solution()
    assert sol.sumIndicesWithKSetBits(nums, k) == expected


# --------------------
# Main Method
# --------------------

def main():
    nums = [5, 10, 1, 5, 2]
    k = 1
    sol = Solution()
    result = sol.sumIndicesWithKSetBits(nums, k)
    print(f"Input nums = {nums}, k = {k}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()

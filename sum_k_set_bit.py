"""
    You are given a 0-indexed integer array nums and an integer k.

    Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
"""

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



if __name__ == "__main__":
    nums = [5, 10, 1, 5, 2]
    k = 1

    sol = Solution()
    result = sol.sumIndicesWithKSetBits(nums, k)

    print("Result:", result)
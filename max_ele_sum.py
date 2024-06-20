"""
    You are given a 0-indexed integer array nums and an integer k.

    Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
"""

import math
class Solution:
    def perfect_subsets(self, n):
      #TODO: write function to find list of perfect square subsets
      pass

  
    def maximumSum(self, nums: List[int]) -> int:
        l = self.perfect_subsets(len(nums))
        s = 0
        for subset in l:
            tmp = sum([nums[i-1] for i in subset])
            if s < tmp:
                s = tmp
        return s

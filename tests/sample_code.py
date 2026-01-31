# Date: 31/01/2026

class Solution:
    def generateSubsets(self, nums, current, index, ans):
        if index == len(nums):
            ans.append(current.copy())
            return
        
        # Include current element
        current.append(nums[index])
        self.generateSubsets(nums, current, index + 1, ans)
        
        # Exclude current element
        current.pop()
        self.generateSubsets(nums, current, index + 1, ans)

    def subsets(self, nums):
        ans = []
        current = []
        self.generateSubsets(nums, current, 0, ans)
        return ans

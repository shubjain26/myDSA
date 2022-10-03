## link: https://binarysearch.com/problems/Largest-Sublist-Sum
## Difficulty: Medium
## First Attempt: No
## Topics: array, Kadane's Algorithm

"""
Approach:

"""


class Solution:
    def solve(self, nums):
        
        max_global = nums[0]
        max_current = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i],max_current+nums[i])
            max_global = max(max_current,max_global)

        return max_global
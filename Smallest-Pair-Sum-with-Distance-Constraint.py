## link: https://binarysearch.com/problems/Smallest-Pair-Sum-with-Distance-Constraint
## Difficulty: Easu
## First Attempt: Yes
## Topics: array

"""
Approach:

"""


class Solution:
    def solve(self, nums):
        max_val = max(nums)
        min_array = [max_val] * len(nums)

        curr_min = nums[-1]
        for i in range(len(nums)):
            ptr = len(nums) - i -1
            curr_min = min(curr_min, nums[ptr])
            min_array[ptr] = curr_min

        global_min = nums[0] + nums[-1]
        for i in range(len(nums)-2):
            curr_min_sum = nums[i] + min_array[i+2]
            global_min = min(global_min,curr_min_sum)


        return global_min

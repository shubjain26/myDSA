"""
Ref: https://leetcode.com/problems/maximum-subarray/

Kadane's Algorithm
Important Question
Iterate from left to right if the current sum is negative, discard the values till now and start from next element.
No matter the value next element, negative sum will always reduce total value anyway.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for i, n in enumerate(nums):                
            
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
            
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
                
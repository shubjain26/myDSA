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
                
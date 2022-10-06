"""
Ref: https://leetcode.com/problems/product-of-array-except-self/

- Topics: Array , Prefix-Sum

Time Complexity: O(n)
Space Complexity : O(n)

Approach: 
    1. Space Complexity O(n)
        - create prefix and postfix products and for every element multiply both to find the result
    2. Space Complexity O(1)
        - Use only result array and write on that twice, left to right and right to left
"""


## Approach 1 : 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums)
        
        pre_init = 1
        for i in range(len(nums)):
            prefix[i] = pre_init
            pre_init = pre_init * nums[i]
            
        post_init = 1
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = post_init
            post_init = post_init * nums[i]
        
        
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]


        return result



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        
        pre_init = 1
        for i in range(len(nums)):
            result[i] = pre_init
            pre_init = pre_init * nums[i]
            
        post_init = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] = post_init * result [i]
            post_init = post_init * nums[i]
        
        return result

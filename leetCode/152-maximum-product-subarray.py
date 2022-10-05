"""
Ref: https://leetcode.com/problems/maximum-product-subarray/
- Difficulty : Medium
- Topics : Array, Dynamic programming

Approach:
    - Keep a min and max at every index because negative min value can become max if next element is negative
    - if n is greater / lesser than the currMax/ currMin then them with n. 
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMax, curMin = 1, 1
        res = max(nums)

        for n in nums:

            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)

            res = max(res, curMax, curMin)

        return res

"""
Ref: https://leetcode.com/problems/trapping-rain-water/

- Topics: Array , prefix postfix

Time Complexity: O(n)
Space Complexity : O(n)

Approach: 
    - Find max from right and max from left
    - Water trapped at an index will be equal to the min(max right, max left) - height[i]
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0 
        if len(height) <= 1:
            return total

        left_max = height[0]
        right_max = height[-1]
        
        premax = [0]*len(height)
        postmax = [0]*len(height)


        for i in range(1,len(height)):            
            premax[i] = max(left_max, height[i])
            left_max = max(left_max, height[i])

        for i in range(len(height)-2,-1,-1):            
            postmax[i] = max(right_max, height[i])
            right_max = max(right_max, height[i])

        for i in range(len(height)):
            total += max(min(premax[i],postmax[i]) - height[i], 0)

            
        return total

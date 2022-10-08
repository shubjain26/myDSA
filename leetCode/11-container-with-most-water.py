"""
Ref: https://leetcode.com/problems/container-with-most-water

- Topics: Array , Two Pointer

Time Complexity: O(n)
Space Complexity : O(1)

Approach: 
    - Use Two pointer
    - Start with left and right end, shift one with lower value
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:

            area = min(height[l], height[r]) * abs(l - r)

            max_area = max(area, max_area)

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return max_area

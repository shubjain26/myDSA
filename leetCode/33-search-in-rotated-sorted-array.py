"""
Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/

- Topics: Array , Binary Search

Time Complexity: O(Log(n))
Space Complexity : O(1)

Approach: 
    - Apply binary search with some conditions to handle different cases
    - Check if middle is falling in left or right side of the sorted array
    - Shift left and right checking the corner elements
        - In the left sorted array if target is smaller than the first element or bigger than the mid then shift right, else shift left
        - In the right sorted array if target is bigger than the last element or smaller than the mid then shift left, else shift right

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        
        while l <= r:
            
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                # left
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            else:
                # right
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

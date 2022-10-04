"""
Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

- Important Question
- Binary Search


Approach : Apply binary search and find pivot value

- Pivot will be the minimum value
- For selecting left or right, choose the side whose corner values are not sorted
[5,6,1,2,3,4]
middle : 2
left arr = [5,6,1]
right arr = [3,4]
in the left arr, corner values 5, 1 are not sorted so the minimum value must be present in this sub array. 
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = int((left + right) / 2)
            if nums[middle] > nums[middle+1]:
                return nums[middle+1]
            
            elif nums[middle-1] > nums[middle] :
                return nums[middle]
            
            else:
                
                if nums[left]  > nums[middle-1]:
                    right = middle - 1
                elif nums[middle+1] > nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
                    
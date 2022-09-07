## link: https://binarysearch.com/problems/Sum-of-Two-Numbers-with-Sorted-List
## Difficulty: Easy
## First Attempt: Yes
## Topics:
"""
Solution Summary: Use Two pointer approach
"""

"""
# Using brute-force approach with binary search on rest of the list

class Solution:
    ## Slow Approach
    def solve(self, nums, k):


        def binary_search(lst, s):

            if len(lst) == 1 and lst[0] ==s :
                return True

            start = 0
            end = len(lst)-1
            found = False
            while start < end :
                mid = int((start+end)/2)
                if lst[start] == s:
                    found = True
                    break
                elif lst[end] == s:
                    found = True
                    break
                elif lst[mid] == s:
                    found = True
                    break
                else:
                    if lst[mid] > s:
                        ## shift left
                        end = mid - 1
                        continue
                    else:
                        start = mid + 1
                        continue

            return found

        result = False
        for i, n in enumerate(nums[:len(nums)-1]):
            reqd = k - n

            if binary_search(nums[i+1:],reqd):
                result = True
                break
            else:
                continue
        return result
"""

# Using two pointer approach 
# begin with start and end pointer , 
# take the sum if start + end > target, move the end pointer to left 
# if start + end < target, move the start pointer to right 

class Solution:
    def solve(self, nums, k):

        left = 0
        right = len(nums) - 1
        result = False
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == k:
                result = True
                break
            elif cur_sum > k:
                right = right - 1
                continue
            else:
                left = left + 1
                continue

        return result

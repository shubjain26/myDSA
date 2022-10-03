## link: https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List
## Difficulty: Easy
## First Attempt: yes
## Topics: Array

"""
Approach: the numbers of the list are chosen from a list 1 to n
We can calc sum of elements in AP. Compare it with actual SUM
The difference will be the extra number
"""

class Solution:
    def solve(self, nums):
        n = len(nums) - 1
        return sum(nums) - (n*(n+1)*(0.5))

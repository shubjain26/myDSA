## link: https://binarysearch.com/problems/Hoppable
## Difficulty: Medium
## First Attempt: No
## Topics: Dynamic Programming

"""
Approach: 
Start from end of the array as goal and then take a step backwards
for every element 
    if i + nums[i] >= goal, it means from that step goal is achievable
        shift the goal to i

if goal is 0 at the end, then return True

"""

class Solution:
    def solve(self, nums):
        
        goal = len(nums) -1
        for i in range(len(nums)-1,-1,-1):

            if i + nums[i] >= goal:
                goal = i
        
        return  goal == 0 
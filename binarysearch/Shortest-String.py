## link: https://binarysearch.com/problems/Shortest-String
## Difficulty: Easy
## First Attempt: Yes
## Topics: array, stack

"""
approach: 
Using a stack (array). and iterate over the string.
if stack is empty or it matches the last element push to the stack.
if it doesn't match then pop from the stack

at the end if anything is left in the stack that will be remaining string.
"""



class Solution:
    def solve(self, s):
        stack = []

        for i,n in enumerate(s):
            if len(stack) == 0:
                stack.append(n)

            elif n == stack[-1]:
                stack.append(n)
            else:
                stack.pop()

        
        return len(stack)

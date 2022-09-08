## link: https://binarysearch.com/problems/Removing-Parentheses
## Difficulty: Medium
## First Attempt: yes
## Topics: String

"""
Approach: 
create a stack, and a filtered_counter
if bracket is opening push to stack
if bracket is closing check if the last bracket was opening bracket, pop from the stack
if bracket is closing but last bracket was not opening, do no push this to stack, just increment the filtered_counter.
at the end if stack is not empty add the len of stack to the filtered_counter, which will be the answer
"""

class Solution:
    def solve(self, s):

        stack = []
        counts = 0

        for p in s:
            if p == "(":
                stack.append(p)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    counts += 1

        total = counts + len(stack)

        return total

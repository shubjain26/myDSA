"""
Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters

- Topics: String, Hash Table, Sliding Window 
- Difficulty : Medium


Time Complexity: O(n)
Space Complexity : O(n)

Approach: 
    Use two pointer left and right
    Use a set to check for duplicates
    Iterate through elements, as right pointer, if character is new , add to the Set
        Else, remove the left pointer element until that character is removed from the Set.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        length = 0
        max_len = 0

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            max_len = max(max_len, len(charSet))

        return max_len

"""
Ref: https://leetcode.com/problems/linked-list-cycle/

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
    Traverse the linked list
    Create Hashtable, keep hash of node as key
    Check at every new node if hash(node) is in it or not.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashtable = {}
        if head is None:
            return False
        
        cursor = head
        cycle = False
        while True:
            
            if hash(cursor) in hashtable:
                cycle = True
                break
            hashtable[hash(cursor)]  = 1
            
            if cursor.next is None:
                break
            else:
                cursor = cursor.next

        return cycle
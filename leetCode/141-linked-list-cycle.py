"""
Ref: https://leetcode.com/problems/linked-list-cycle/

Difficulty: Easy

Topic: Linked List, Hash Table, Two Pointers

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
    Hashtable:
        Traverse the linked list
        Create Hashtable, keep hash of node as key
        Check at every new node if hash(node) is in it or not.
    Slow and Fast Pointer:
        - Also called Floyd's tortoise and hare
        - create two pointers, move slow pointer by one and fast pointer by two
        - if list has cycle they'll eventually come to the same node
        - This works because every iteration the effective distance reduces by 1
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

## Floyd's tortoise and hare 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        cycle = False
        slow = head
        fast = head.next

        while True:
            if slow.next is None or fast.next is None:
                break
            elif slow == fast:
                cycle = True
                break
            else:
                slow = slow.next
                fast = fast.next.next
                if fast is None:
                    break

        return cycle
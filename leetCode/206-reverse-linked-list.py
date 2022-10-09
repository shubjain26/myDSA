"""
Ref: https://leetcode.com/problems/reverse-linked-list/

Difficulty: Easy

Topic: Linked List, Recursion

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
    Traverse the linked list
    Keep a prev_node as Null initially (this will be last node of reversed list).
    For every node assign the prev_node as next node in reverse list.
    prev_node is the final reversed list.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        cursor = head
        prev_node = None
        while True:
            prev_node = ListNode(cursor.val, prev_node)
            if not cursor.next is None:
                cursor = cursor.next
            else:
                break
        
        return prev_node

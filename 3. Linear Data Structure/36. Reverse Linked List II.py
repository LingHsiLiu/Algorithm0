# 36. Reverse Linked List II
# Reverse a linked list from position m to n.

# Example
# Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.

# Challenge
# Reverse it in-place and in one-pass

# Notice
# Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here

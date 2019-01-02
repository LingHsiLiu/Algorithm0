# 174. Remove Nth Node From End of List
# Given a linked list, remove the nth node from the end of list and return its head.

# Example
# Given linked list: 1->2->3->4->5->null, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5->null.


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here

# 452. Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.

# Example
# Given 1->2->3->3->4->5->3, val = 3, you should return the list as 1->2->4->5

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here

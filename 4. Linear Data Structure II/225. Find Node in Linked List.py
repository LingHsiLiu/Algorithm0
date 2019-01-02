# 225. Find Node in Linked List
# Find a node with given value in a linked list. Return null if not exists.

# Example
# Given 1->2->3 and value = 3, return the last node.

# Given 1->2->3 and value = 4, return null.

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the head of linked list.
    @param: val: An integer.
    @return: a linked node or null.
    """
    def findNode(self, head, val):
        # write your code here

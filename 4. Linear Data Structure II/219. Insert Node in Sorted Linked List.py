# 219. Insert Node in Sorted Linked List
# Insert a node in a sorted linked list.

# Example
# Given list = 1->4->6->8 and val = 5.

# Return 1->4->5->6->8.

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here

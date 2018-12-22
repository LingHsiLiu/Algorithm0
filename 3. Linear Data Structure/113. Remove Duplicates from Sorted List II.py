# 113. Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here

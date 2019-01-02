# 217. Remove Duplicates from Unsorted List
# Write code to remove duplicates from an unsorted linked list.

# Example
# Given 1->3->2->1->4.

# Return 1->3->2->4

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
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here

# 98. Sort List
# Sort a linked list in O(n log n) time using constant space complexity.

# Example
# Given 1->3->2->null, sort it to 1->2->3->null.

# Challenge
# Solve it by merge sort & quick sort separately.

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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here

# 177. Convert Sorted Array to Binary Search Tree With Minimal Height
# Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.

# Example
# Given [1,2,3,4,5,6,7], return

#      4
#   /   \
#   2     6
#  / \    / \
# 1   3  5   7

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here

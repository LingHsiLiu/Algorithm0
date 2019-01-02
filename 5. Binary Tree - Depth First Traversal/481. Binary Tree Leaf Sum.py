# 481. Binary Tree Leaf Sum
# Given a binary tree, calculate the sum of leaves.

# Example
# Given

#     1
#   / \
#   2   3
#  /
# 4
# return 7.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here

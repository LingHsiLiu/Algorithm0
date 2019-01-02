# 87. Remove Node in Binary Search Tree
# Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

# Example
# Given binary search tree:

#     5
#   / \
#   3   6
#  / \
# 2   4
# Remove 3, you can either return:

#     5
#   / \
#   2   6
#   \
#     4

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here

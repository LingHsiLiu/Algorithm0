# 482. Binary Tree Level Sum
# Given a binary tree and an integer which is the depth of the target level.

# Calculate the sum of the nodes in the target level.

# Example
# Given a binary tree:

#      1
#   /   \
#   2     3
#  / \   / \
# 4   5 6   7
#   /       \
#   8         9
# For depth = 2, return 5.
# For depth = 3, return 22.
# For depth = 4, return 17.

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
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here

# 469. Same Tree
# Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

# Example
#     1             1
#   / \           / \
#   2   2   and   2   2
#  /             /
# 4             4
# are identical.

#     1             1
#   / \           / \
#   2   3   and   2   3
#  /               \
# 4                 4
# are not identical.


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here

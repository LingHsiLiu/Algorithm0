# 470. Tweaked Identical Binary Tree
# Check two given binary trees are identical or not. Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.

# Example
#     1             1
#   / \           / \
#   2   3   and   3   2
#  /                   \
# 4                     4
# are identical.

#     1             1
#   / \           / \
#   2   3   and   3   2
#  /             /
# 4             4
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
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # write your code here

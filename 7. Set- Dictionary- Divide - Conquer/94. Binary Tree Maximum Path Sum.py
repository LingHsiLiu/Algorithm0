# 94. Binary Tree Maximum Path Sum
# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# Example
# Given the below binary tree:

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        maxSum, _ = self.maxPathHelper(root)
        return maxSum
        
    def maxPathHelper(self, root):
        if root is None:
            return  -sys.maxsize - 1, 0
        
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)
        
        return maxpath, single

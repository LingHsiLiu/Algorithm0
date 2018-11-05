# 68. Binary Tree Postorder Traversal
# Given a binary tree, return the postorder traversal of its nodes' values.

# Example
# Given binary tree {1,#,2,3},


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        self.results = []
        self.helper(root)
        return self.results
        
    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.helper(root.right)
        self.results.append(root.val)

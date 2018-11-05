#66. Binary Tree Preorder Traversal

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        self.results = []
        self.helper(root)
        return self.results
        
    def helper(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.helper(root.left)
        self.helper(root.right)

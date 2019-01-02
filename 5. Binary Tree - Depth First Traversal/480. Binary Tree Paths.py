# 480. Binary Tree Paths
# Given a binary tree, return all root-to-leaf paths.

# Example
# Given the following binary tree:

#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# [
#   "1->2->5",
#   "1->3"
# ]

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
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)] ##回傳先前subtree
        
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
            
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
        
        return paths
        

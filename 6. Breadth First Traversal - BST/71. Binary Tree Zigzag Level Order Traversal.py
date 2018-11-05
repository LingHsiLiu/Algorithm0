# 71. Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its nodes
# ' values. (ie, from left to right, then right to left for the next level and alternate between).

# Example
# Given binary tree {3,9,20,#,#,15,7},

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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        self.results = []
        self.preorder(root, 0, self.results)
        return self.results
    
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0: 
                res[level].append(root.val)
            else: 
                res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)



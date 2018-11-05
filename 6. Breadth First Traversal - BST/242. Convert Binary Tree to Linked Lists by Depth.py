# 242. Convert Binary Tree to Linked Lists by Depth
# Given a binary tree, design an algorithm which creates a linked list of 
# all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []
        self.dfs(root, 1, result)
        return result
        

    def dfs(self, root, depth, result):
        if root is None:
            return
        node = ListNode(root.val)
        if len(result) < depth:
            result.append(node)
            print(result)
        else:
            node.next = result[depth-1]
            result[depth-1] = node
            print(result)
        
        self.dfs(root.right, depth + 1, result)
        self.dfs(root.left, depth + 1, result)

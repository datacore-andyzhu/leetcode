from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_set = set(nodes)

        def dfs(node, nodesSet):

            if not node:
                return None
            if node in nodesSet:
                return node
            left = dfs(node.left, nodesSet)
            right = dfs(node.right, nodesSet)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
        return dfs(root, nodes_set)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.existsP = False
        self.existsQ = False

    def lca(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if root.val == p.val:
            self.existsP = True
            return root

        if root.val == q.val:
            self.existsQ = True
            return root

        if left and right:
            return root
        else:
            return left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.lca(root, p, q)

        return result if self.existsP and self.existsQ else None

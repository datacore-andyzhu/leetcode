# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """ Solution 1"""
        # def inorder(root):
        #     if not root:
        #         return None
        #     stack = []
        #     prev = None
        #     while stack or root:
        #         while root:
        #             stack.append(root)
        #             root = root.left
        #         root = stack.pop()
        #         if prev is not None and prev.val == p.val:
        #             return root
        #         prev = root
        #         root = root.right
        #     return None
        # return inorder(root)

        """ Solution 2 """
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

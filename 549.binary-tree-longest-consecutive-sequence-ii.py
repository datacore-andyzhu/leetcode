# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0, 0
            leftlen, leftDown, leftUp = dfs(root.left)
            rightlen, rightDown, rightUp = dfs(root.right)

            length, down, up = 0, 0, 0
            if root.left and root.val + 1 == root.left.val:
                down = max(down, leftDown+1)
            if root.left and root.val - 1 == root.left.val:
                up = max(up, leftUp + 1)

            if root.right and root.val + 1 == root.right.val:
                down = max(down, rightDown+1)
            if root.right and root.val - 1 == root.right.val:
                up = max(up, rightUp+1)

            length = max(down+1+up, leftlen, rightlen)

            return length, down, up

        if not root:
            return 0
        length, _, _ = dfs(root)
        return length
"""
https://www.youtube.com/watch?v=p3tSOngKku8&list=PL5Eeqoo6exqUghcOgA4sBRRDg-cObFBQW&index=3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxConsecutiveLength = 0
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0

            curr_max = 1
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            if root.left and root.val == root.left.val-1:
                curr_max = max(curr_max, leftMax+1)

            if root.right and root.val == root.right.val-1:
                curr_max = max(curr_max, rightMax+1)

            self.maxConsecutiveLength = max(
                self.maxConsecutiveLength, curr_max)
            return curr_max

        dfs(root)
        return self.maxConsecutiveLength

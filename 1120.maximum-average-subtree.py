# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def dfs(root):
            if not root:
                return 0, 0
            leftsum, leftsize = dfs(root.left)
            rightsum, rightsize = dfs(root.right)

            total_sum = leftsum + rightsum + root.val
            total_size = leftsize + 1 + rightsize

            average = total_sum / total_size

            self.maxAVG = max(self.maxAVG, average)
            return total_sum, total_size

        self.maxAVG = float('-inf')
        if not root:
            return 0
        dfs(root)

        return self.maxAVG

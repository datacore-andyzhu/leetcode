# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            nonlocal count
            if not root:
                return 0
            left_sum = postorder(root.left)
            right_sum = postorder(root.right)
            if root.val == (left_sum + right_sum):
                count += 1
            return left_sum + right_sum + root.val
        count = 0
        postorder(root)
        return count

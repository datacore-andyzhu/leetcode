# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """ Solution 1 """
        # minVal = float('inf')
        # ans = -1
        # if not root:
        #     return None
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if abs(target-node.val) < minVal:
        #         minVal = abs(target-node.val)
        #         ans = node.val
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return ans

        """ Solution 2"""
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if prev <= target < root.val:
                return min(prev, root.val, key=lambda x: abs(target-x))
            prev = root.val
            root = root.right
        return prev

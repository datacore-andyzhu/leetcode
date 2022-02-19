# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class DS:
    def __init__(self, isBST, size, maxVal, minVal):
        self.isBST = isBST
        self.size = size
        self.maxVal = maxVal
        self.minVal = minVal


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        INT_MAX = float('inf')
        INT_MIN = float('-inf')
        ans = 0

        def dfs(root):
            if not root:
                return DS(True, 0, INT_MIN, INT_MAX)
            left = dfs(root.left)
            right = dfs(root.right)
            if left.maxVal < root.val < right.minVal and left.isBST and right.isBST:
                _size = 1 + left.size + right.size
                _minVal = min(root.val, left.minVal)
                _maxVal = max(root.val, right.maxVal)
                return DS(True, _size, _maxVal, _minVal)
            return DS(False, max(left.size, right.size), INT_MIN, INT_MAX)
        return dfs(root).size
        # return ans

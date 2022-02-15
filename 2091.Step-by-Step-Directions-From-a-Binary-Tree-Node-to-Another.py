# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def buildPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            if buildPath(root.left, target, path):
                path.append('L')
                return True
            elif buildPath(root.right, target, path):
                path.append('R')
                return True
            return False

        startPath = []
        endPath = []
        buildPath(root, startValue, startPath)
        buildPath(root, destValue, endPath)
        # print(startPath)
        # print(endPath)
        while len(startPath) != 0 and len(endPath) != 0 and startPath[-1] == endPath[-1]:
            startPath.pop()
            endPath.pop()
        endPath.reverse()
        return ''.join(['U']*len(startPath)+endPath)

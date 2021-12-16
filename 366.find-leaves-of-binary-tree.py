# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def getHeight(root):
            if not root:
                return -1

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)

            curr_height = max(leftHeight, rightHeight) + 1

            if len(result) == curr_height:
                result.append([])
            result[curr_height].append(root.val)

            return curr_height

        result = []

        getHeight(root)

        return result

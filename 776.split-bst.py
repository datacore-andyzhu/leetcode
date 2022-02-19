# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return None, None
        elif root.val <= target:
            bns = self.splitBST(root.right, target)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, target)
            root.left = bns[1]
            return bns[0], root

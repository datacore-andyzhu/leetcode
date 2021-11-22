# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc tags=tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
#
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSame(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # def contains_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if root is None and subRoot is None:
    #         return True
    #     if root is None and subRoot is not None or root is not None and subRoot is None:
    #         return False
    #     if root.val == subRoot.val:
    #         if self.contains_subtree(root.left, subRoot.left) and self.contains_subtree(root.right, subRoot.right):
    #             return True
    #     return False

    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return False

    #     if root.val == subRoot.val:
    #         if self.contains_subtree(root, subRoot):
    #             return True

    #     if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
    #         return True

    #     return False
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,4,5,1,2], subRoot = [4,1,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSubtree(listToTreeNode(
        [3, 4, 5, 1, 2]), listToTreeNode([4, 1, 2]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSubtree(listToTreeNode(
        [3, 4, 5, 1, 2, None, None, None, None, 0]), listToTreeNode([4, 1, 2]))))
    print()

    pass
# @lc main=end

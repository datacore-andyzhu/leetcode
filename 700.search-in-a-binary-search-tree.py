# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#


# @lc tags=Unknown

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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 2')
    print('Exception :')
    print('[2,1,3]')
    print('Output :')
    print(str(Solution().searchBST(listToTreeNode([4, 2, 7, 1, 3]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 5')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().searchBST(listToTreeNode([4, 2, 7, 1, 3]), 5)))
    print()

    pass
# @lc main=end

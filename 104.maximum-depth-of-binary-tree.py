# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc tags=tree;depth-first-search

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ Option 1: use the recursive method """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxDepth(
        listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([1, None, 2]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([0]))))
    print()

    pass
# @lc main=end

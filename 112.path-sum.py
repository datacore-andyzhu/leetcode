# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        else:
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasPathSum(listToTreeNode(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3], targetSum = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasPathSum(listToTreeNode([1, 2, 3]), 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2], targetSum = 0')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasPathSum(listToTreeNode([1, 2]), 0)))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = -1

        def dfs(root, curr):
            if not root:
                return
            if root.val != curr:
                if self.ans == -1:
                    self.ans = root.val
                else:
                    self.ans = min(self.ans, root.val)
                return

            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root, root.val)
        return self.ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,2,5,null,null,5,7]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findSecondMinimumValue(
        listToTreeNode([2, 2, 5, None, None, 5, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,2,2]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findSecondMinimumValue(listToTreeNode([2, 2, 2]))))
    print()

    pass
# @lc main=end

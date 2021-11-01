# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#


# @lc tags=dynamic-programming;tree;depth-first-search

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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, n):
            


# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [8,5,1,7,10,12]')
    print('Exception :')
    print('[8,5,10,1,7,null,12]')
    print('Output :')
    print(str(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])))
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = [1,3]')
    print('Exception :')
    print('[1,null,3]')
    print('Output :')
    print(str(Solution().bstFromPreorder([1, 3])))
    print()

    pass
# @lc main=end

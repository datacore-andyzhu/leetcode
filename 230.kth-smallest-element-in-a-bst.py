# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc tags=binary-search;tree

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 0
        res = 0

        def traverse(root, k):
            nonlocal rank
            nonlocal res
            if root is None:
                return None
            traverse(root.left, k)
            rank += 1
            if rank == k:
                res = root.val
                return
            traverse(root.right, k)
        # main function
        traverse(root, k)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,1,4,null,2], k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kthSmallest(listToTreeNode([3, 1, 4, None, 2]), 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,null,1], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().kthSmallest(
        listToTreeNode([5, 3, 6, 2, 4, None, None, 1]), 3)))
    print()

    pass
# @lc main=end

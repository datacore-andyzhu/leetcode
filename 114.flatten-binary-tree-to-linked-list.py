# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if root is None:
            return None
        # recursive call to flattern left side and right side
        self.flatten(root.left)
        self.flatten(root.right)

        # now left side and right side are flatterned,
        # we need to set left side to be root's new right child
        # and link root original right child at the end of left child
        left_side = root.left
        right_side = root.right

        # set the root's new right child to be old left child
        # and rest root's left child to be None
        root.left = None
        root.right = left_side
        # now trace from the root until root's right child is Null
        # then connect to root's original right child
        p = root
        while p.right:
            p = p.right
        p.right = right_side

        return root

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,5,3,4,null,6]')
    print('Exception :')
    print('[1,null,2,null,3,null,4,null,5,null,6]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([1, 2, 5, 3, 4, None, 6]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([0]))))
    print()

    pass
# @lc main=end

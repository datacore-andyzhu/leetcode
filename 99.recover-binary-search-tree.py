# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traversale(root):
            nonlocal x, y, prev
            if not root:
                return None
            traversale(root.left)

            if prev is not None and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
            prev = root
            traversale(root.right)

        def swap(x, y):
            temp = x.val
            x.val = y.val
            y.val = temp

        prev, x, y = None, None, None
        traversale(root)
        swap(x, y)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,null,null,2]')
    print('Exception :')
    print('[3,1,null,null,2]')
    print('Output :')
    print(str(Solution().recoverTree(listToTreeNode([1,3,None,None,2]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [3,1,4,null,null,2]')
    print('Exception :')
    print('[2,1,4,null,null,3]')
    print('Output :')
    print(str(Solution().recoverTree(listToTreeNode([3,1,4,None,None,2]))))
    print()
    
    pass
# @lc main=end

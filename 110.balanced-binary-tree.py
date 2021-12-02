# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return True
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isBalanced(listToTreeNode([3,9,20,None,None,15,7]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,3,3,null,null,4,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isBalanced(listToTreeNode([1,2,2,3,3,None,None,4,4]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isBalanced(listToTreeNode([]))))
    print()
    
    pass
# @lc main=end
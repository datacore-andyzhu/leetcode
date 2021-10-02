# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], k = 9')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([5,3,6,2,4,None,7]),9)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], k = 28')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([5,3,6,2,4,None,7]),28)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [2,1,3], k = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2,1,3]),4)))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('root = [2,1,3], k = 1')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2,1,3]),1)))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('root = [2,1,3], k = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2,1,3]),3)))
    print()
    
    pass
# @lc main=end
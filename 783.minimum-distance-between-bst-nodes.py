# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """ solution 1 """
        def traversal(curr):
            nonlocal pre, result
            if not curr:
                return
            traversal(curr.left)
            if pre is not None:
                result = min(result, curr.val-pre.val)
            pre = curr
            traversal(curr.right)

        pre = None
        result = float('inf')
        traversal(root)
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,6,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDiffInBST(listToTreeNode([4,2,6,1,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,0,48,null,null,12,49]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDiffInBST(listToTreeNode([1,0,48,None,None,12,49]))))
    print()
    
    pass
# @lc main=end

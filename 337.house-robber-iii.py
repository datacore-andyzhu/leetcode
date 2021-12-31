# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob_tree(root):
            if not root:
                return (0,0) # first element is for not rob the node
                                # 2nd element is for rob the node
            left = rob_tree(root.left)
            right = rob_tree(root.right)
            # rob the root
            val1 = root.val + left[0] + right[0]
            # not rob the root
            val2 = max(left) + max(right)
            return (val2, val1)
        result = rob_tree(root)
        return max(result)

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,2,3,null,3,null,1]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().rob(listToTreeNode([3,2,3,None,3,None,1]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [3,4,5,1,3,null,1]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().rob(listToTreeNode([3,4,5,1,3,None,1]))))
    print()
    
    pass
# @lc main=end
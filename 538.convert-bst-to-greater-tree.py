# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            nonlocal total
            if root is None:
                return None
            # reverse the BST and then add to accumlate the all the value so far
            # and add to the node
            traverse(root.right)
            total += root.val
            root.val = total
            traverse(root.left)

        total = 0
        traverse(root)
        return root
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    print('Exception :')
    print('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')
    print('Output :')
    print(str(Solution().convertBST(listToTreeNode([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [0,null,1]')
    print('Exception :')
    print('[1,null,1]')
    print('Output :')
    print(str(Solution().convertBST(listToTreeNode([0,None,1]))))
    print()
    
    pass
# @lc main=end

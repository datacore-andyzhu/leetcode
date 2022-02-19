# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#


# @lc tags=math

# @lc imports=start
from tkinter.tix import Tree
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # def inOrder(root):
        #     if root:
        #         yield from inOrder(root.left)
        #         yield root.val
        #         yield from inOrder(root.right)
        # ans = curr = TreeNode(None)
        # for v in inOrder(root):
        #     curr.right = TreeNode(v)
        #     curr = curr.right
        # return ans.right

        """ Solution 2 """
        def inOrder(root):
            if root:
                inOrder(root.left)
                root.left = None
                self.curr.right = root
                self.curr = self.curr.right
                inOrder(root.right)
        ans = self.curr = TreeNode(None)
        inOrder(root)
        return ans.right
                
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,8,1,null,null,null,7,9]')
    print('Exception :')
    print('[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]')
    print('Output :')
    print(str(Solution().increasingBST(listToTreeNode([5,3,6,2,4,None,8,1,None,None,None,7,9]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [5,1,7]')
    print('Exception :')
    print('[1,null,5,null,7]')
    print('Output :')
    print(str(Solution().increasingBST(listToTreeNode([5,1,7]))))
    print()
    
    pass
# @lc main=end
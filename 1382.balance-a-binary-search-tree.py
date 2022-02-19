# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#


# @lc tags=Unknown

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        nums = inorder(root)

        def BST(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])

            mid = len(nums)//2
            root_node = TreeNode(nums[mid])
            root_node.left = BST(nums[:mid])
            root_node.right = BST(nums[mid+1:])
            return root_node
        return BST(nums)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,null,3,null,4,null,null]')
    print('Exception :')
    print('[2,1,3,null,null,null,4]')
    print('Output :')
    print(str(Solution().balanceBST(listToTreeNode([1,None,2,None,3,None,4,None,None]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('[2,1,3]')
    print('Output :')
    print(str(Solution().balanceBST(listToTreeNode([2,1,3]))))
    print()
    
    pass
# @lc main=end

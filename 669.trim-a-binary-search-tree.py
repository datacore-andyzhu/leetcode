# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """ Solution 1: recursive """
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root

        """ Solution 2: Iterative """
        if not root:
            return None
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

        curr = root
        while curr:
            while curr.left and curr.left.val < low:
                curr.left = curr.left.right
            curr = curr.left

        curr = root
        while curr:
            while curr.right and curr.right.val > high:
                curr.right = curr.right.left
            curr = curr.right

        return root
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,0,2], low = 1, high = 2')
    print('Exception :')
    print('[1,null,2]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([1,0,2]),1,2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [3,0,4,null,2,null,null,1], low = 1, high = 3')
    print('Exception :')
    print('[3,2,null,1]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([3,0,4,None,2,None,None,1]),1,3)))
    print()
    
    pass
# @lc main=end

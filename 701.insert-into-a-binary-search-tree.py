# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ Option 1: Use the recursive method """
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 5')
    print('Exception :')
    print('[4,2,7,1,3,5]')
    print('Output :')
    print(str(Solution().insertIntoBST(listToTreeNode([4, 2, 7, 1, 3]), 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [40,20,60,10,30,50,70], val = 25')
    print('Exception :')
    print('[40,20,60,10,30,50,70,null,null,25]')
    print('Output :')
    print(str(Solution().insertIntoBST(
        listToTreeNode([40, 20, 60, 10, 30, 50, 70]), 25)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [4,2,7,1,3,null,null,null,null,null,null], val = 5')
    print('Exception :')
    print('[4,2,7,1,3,5]')
    print('Output :')
    print(str(Solution().insertIntoBST(listToTreeNode(
        [4, 2, 7, 1, 3, None, None, None, None, None, None]), 5)))
    print()

    pass
# @lc main=end

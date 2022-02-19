# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#


# @lc tags=math;dynamic-programming

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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """ Soltuion 1 """
        # ans = 0
        # def inorder(root):
        #     if not root:
        #         return None
        #     inorder(root.left)
        #     if low <= root.val <= high:
        #         ans += root.val
        #     inorder(root.right)
        # inorder(root)
        # return ans
        """ Solution 2 """
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) \
            + self.rangeSumBST(root.right, low, high)

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [10,5,15,3,7,null,18], low = 7, high = 15')
    print('Exception :')
    print('32')
    print('Output :')
    print(str(Solution().rangeSumBST(
        listToTreeNode([10, 5, 15, 3, 7, None, 18]), 7, 15)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().rangeSumBST(listToTreeNode(
        [10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10)))
    print()

    pass
# @lc main=end

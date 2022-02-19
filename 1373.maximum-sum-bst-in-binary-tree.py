# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
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


class DS:
    def __init__(self, sumx, minVal, maxVal, isBST):
        self.sumx = sumx
        self.minVal = minVal
        self.maxVal = maxVal
        self.isBST = isBST


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            # Null node is BST
            if not node:
                return DS(0, float('inf'), float('-inf'), True)
            left = dfs(node.left)
            right = dfs(node.right)

            if left.isBST and right.isBST and left.maxVal < node.val < right.minVal:
                _sumx = node.val + left.sumx + right.sumx
                _minVal = min(node.val, left.minVal)
                _maxVal = max(node.val, right.maxVal)
                ans = max(ans, _sumx)
                return DS(_sumx, _minVal, _maxVal, True)
            return DS(max(left.sumx, right.sumx), float('inf'), float('-inf'), False)

        ans = 0
        print(dfs(root).sumx)
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().maxSumBST(listToTreeNode(
        [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [4,3,null,1,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxSumBST(listToTreeNode([4, 3, None, 1, 2]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [-4,-2,-5]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxSumBST(listToTreeNode([-4, -2, -5]))))
    print()

    pass
# @lc main=end

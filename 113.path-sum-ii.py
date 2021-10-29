# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []

        def helper(root, targetSum, path):
            if not root.left and not root.right and targetSum == 0:
                # path.append(root.val)
                results.append(path.copy())
                return
            if root.left:
                path.append(root.left.val)
                helper(root.left, targetSum-root.left.val, path)
                path.pop()
            if root.right:
                path.append(root.right.val)
                helper(root.right, targetSum-root.right.val, path)
                path.pop()
        if root is not None:
            helper(root, targetSum-root.val, [root.val])
        return results
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22')
    print('Exception :')
    print('[[5,4,11,2],[5,8,4,5]]')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3], targetSum = 5')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([1, 2, 3]), 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2], targetSum = 0')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([1, 2]), 0)))
    print()

    pass
# @lc main=end

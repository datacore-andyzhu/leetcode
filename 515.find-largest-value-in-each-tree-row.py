# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#


# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
import collections
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        queue = collections.deque([root])
        while queue:
            level_size = len(queue)
            level_max = float('-inf')
            for _ in range(level_size):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,2,5,3,null,9]')
    print('Exception :')
    print('[1,3,9]')
    print('Output :')
    print(str(Solution().largestValues(
        listToTreeNode([1, 3, 2, 5, 3, None, 9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3]')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1, 2, 3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1, None, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([]))))
    print()

    pass
# @lc main=end

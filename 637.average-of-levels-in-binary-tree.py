# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#


# @lc tags=tree

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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        queue = collections.deque([root])
        result = []
        while queue:
            level_size = len(queue)
            sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum/level_size)
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('[3.00000,14.50000,11.00000]')
    print('Output :')
    print(str(Solution().averageOfLevels(
        listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,9,20,15,7]')
    print('Exception :')
    print('[3.00000,14.50000,11.00000]')
    print('Output :')
    print(str(Solution().averageOfLevels(listToTreeNode([3, 9, 20, 15, 7]))))
    print()

    pass
# @lc main=end

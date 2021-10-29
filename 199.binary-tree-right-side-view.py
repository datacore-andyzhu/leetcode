# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        queue = collections.deque([root])
        result = []

        while queue:
            temp = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp[-1])

        return result


# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,5,null,4]')
    print('Exception :')
    print('[1,3,4]')
    print('Output :')
    print(str(Solution().rightSideView(
        listToTreeNode([1, 2, 3, None, 5, None, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,null,3]')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().rightSideView(listToTreeNode([1, None, 3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().rightSideView(listToTreeNode([]))))
    print()

    pass
# @lc main=end

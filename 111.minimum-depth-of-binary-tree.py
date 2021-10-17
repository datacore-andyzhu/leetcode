# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        bfs = collections.deque([root])
        depth = 1
        while bfs:
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            depth += 1
        return depth

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDepth(
        listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,null,3,null,4,null,5,null,6]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().minDepth(listToTreeNode(
        [2, None, 3, None, 4, None, 5, None, 6]))))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#


# @lc tags=stack;tree;breadth-first-search

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        bfs = collections.deque([root])
        results = []
        level = 1
        while bfs:
            curr = []
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                curr.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            if level % 2 == 0:
                curr = reversed(curr)

            results.append(curr)
            level += 1

        return results
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('[[3],[20,9],[15,7]]')
    print('Output :')
    print(str(Solution().zigzagLevelOrder(
        listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().zigzagLevelOrder(listToTreeNode([1]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().zigzagLevelOrder(listToTreeNode([]))))
    print()

    pass
# @lc main=end

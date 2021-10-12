# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc tags=tree;breadth-first-search

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        result = []
        bfs = collections.deque([root])
        while bfs:
            result.append([]) # pay attention of this code, becasue we want
                                # to return multi-dimension array
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                result[-1].append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return result
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('[[3],[9,20],[15,7]]')
    print('Output :')
    print(str(Solution().levelOrder(listToTreeNode([3,9,20,None,None,15,7]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().levelOrder(listToTreeNode([1]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().levelOrder(listToTreeNode([]))))
    print()
    
    pass
# @lc main=end
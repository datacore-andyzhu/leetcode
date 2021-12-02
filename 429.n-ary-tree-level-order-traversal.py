# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#


# @lc tags=Unknown

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
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        queue = collections.deque([root])
        result = []
        while queue:
            level_size = len(queue)
            temp = []
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                for child in node.children:
                    if child:
                        queue.append(child)
            result.append(temp)
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,3,2,4,null,5,6]')
    print('Exception :')
    print('[[1],[3,2,4],[5,6]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root =[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]')
    print('Exception :')
    print('[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end

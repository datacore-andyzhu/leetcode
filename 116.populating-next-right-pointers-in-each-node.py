# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#


# @lc tags=tree;depth-first-search

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
from typing import *

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """ Option 1: Use recursive method """
        # def connectNodes(node1, node2):
        #     # base case
        #     if node1 is None or node2 is None:
        #         return None
        #     node1.next = node2

        #     # connecting nodes from same parent
        #     connectNodes(node1.left, node1.right)
        #     connectNodes(node2.left, node2.right)
        #     # connecting nodes from different parent
        #     connectNodes(node1.right, node2.left)

        # if root is None:
        #     return None
        # connectNodes(root.left, root.right)
        # return root

        """ Option 2: Use iterative/level order traversal (BFS) method """
        if root is None:
            return None
        bfs = collections.deque([(root,0)])
        current_processing_level = 0
        prev = None
        while bfs:
            level_size = len(bfs)
            for _ in range(level_size):
                node, level = bfs.popleft()
                if current_processing_level < level:
                    current_processing_level += 1
                    prev = node
                elif current_processing_level == level and current_processing_level != 0:
                    prev.next = node
                    prev = prev.next
                if node.left:
                    bfs.append((node.left, level+1))
                if node.right:
                    bfs.append((node.right, level+1))
        return root

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,6,7]')
    print('Exception :')
    print('[1,#,2,3,#,4,5,6,7,#]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    pass
# @lc main=end

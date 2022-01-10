# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#


# @lc tags=hash-table;linked-list

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

# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self) -> None:
        self.visited = {}

    def copyNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        newNode = Node(curr.val)
        self.visited[curr] = newNode

        while curr is not None:
            newNode.next = self.copyNode(curr.next)
            newNode.random = self.copyNode(curr.random)

            curr = curr.next
            newNode = newNode.next
        return self.visited[head]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [[7,null],[13,0],[11,4],[10,2],[1,0]]')
    print('Exception :')
    print('[[7,null],[13,0],[11,4],[10,2],[1,0]]')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [[1,1],[2,1]]')
    print('Exception :')
    print('[[1,1],[2,1]]')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [[3,null],[3,0],[3,null]]')
    print('Exception :')
    print('[[3,null],[3,0],[3,null]]')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    pass
# @lc main=end

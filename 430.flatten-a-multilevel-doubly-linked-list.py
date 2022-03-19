# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#


# @lc tags=Unknown

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
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ Solution 1 """
#         if not head:
#             return head
#         dummyhead = Node(0, None, head, None)
#         self.flatten_dfs(dummyhead, head)
#         dummyhead.next.prev = None
#         return dummyhead.next

#     def flatten_dfs(self, prev, curr):
#         if not curr:
#             return prev
#         curr.prev = prev
#         prev.next = curr

#         tempNext = curr.next
#         tail = self.flatten_dfs(curr, curr.child)
#         curr.child = None
#         return self.flatten_dfs(tail, tempNext)

        """ Solution 2 """

        if not head:
            return None
        dummyhead = Node(0, None, head, None)
        prev = dummyhead
        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        dummyhead.next.prev = None
        return dummyhead.next
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]')
    print('Exception :')
    print('[1,2,3,7,8,11,12,9,10,4,5,6]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,null,3]')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    pass
# @lc main=end

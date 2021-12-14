# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """ Solution 1: O(N) space """
        # def bfs(root):
        #     if root is None:
        #         return
        #     queue = collections.deque([root])

        #     while queue:
        #         tmp = []
        #         level_size = len(queue)
        #         for _ in range(level_size):
        #             node = queue.popleft()
        #             tmp.append(node)

        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)
        #         i = 0
        #         while i < len(tmp) - 1:
        #             tmp[i].next = tmp[i+1]
        #             i += 1
        #     return root
        # if root is None:
        #     return None
        # return bfs(root)
        """ Solution 2: O(1) space """
        if not root:
            return None
        curr = root
        while curr:
            # while processing current level,
            # prepare for the next level
            # create a sentinal node as the dummy head
            # also use pre to create the next relationship for next level
            dummyHead = ListNode(0)
            pre = dummyHead
            while curr:
                if curr.left:
                    # at first time, pre is the dummyhead then dummy head to point
                    # to left child of current ndoe
                    pre.next = curr.left
                    # now pre has the value, it can be used to establish the 
                    # next relationship
                    pre = pre.next
                if curr.right:
                    # if current node does not have left child
                    # pre (the dummy head) will point to the right chold
                    
                    pre.next = curr.right
                    # point to the next node
                    pre = pre.next
                # traverse the current level
                curr = curr.next
            # current level is completed, now since we have already use the 
            # pre establish the next level linked list
            # we can use the dummyhead.next to get to the first node of the next level
            curr = dummyHead.next
        
        return root
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,null,7]')
    print('Exception :')
    print('[1,#,2,3,#,4,5,7,#]')
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

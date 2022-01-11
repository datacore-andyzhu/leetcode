# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#


# @lc tags=linked-list

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # because we do not know the previous node
        # let's copy the next node value
        # to current node, and point the
        # current node to the node after the current next node
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,5,1,9], node = 5')
    print('Exception :')
    print('[4,1,9]')
    print('Output :')
    print(str(Solution().deleteNode(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [4,5,1,9], node = 1')
    print('Exception :')
    print('[4,5,9]')
    print('Output :')
    print(str(Solution().deleteNode(1)))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc tags=linked-list

# @lc imports=start
from os import curdir
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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Solution 1: recursive approach """
        # if head is None or head.next is None:
        #     return head
        # next = head.next
        # head.next = self.swapPairs(next.next)
        # next.next = head

        # return next

        """ Solution 2: Iterative apporach """
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        while prev.next and prev.next.next:
            curr = prev.next
            middle = curr.next
            temp = middle.next

            prev.next = middle
            middle.next = curr
            curr.next = temp

            prev = curr
        return dummyHead.next
        """ recursive wrote by myself """
        # if head is None or head.next is None:
        #     return head
        # # first grapb head.next pointer
        # _next = head.next
        # # current head,next point to the recursive call to head.next.next
        # head.next = self.swapPairs(_next.next)
        # # we need to point the _next.next to the old head
        # _next.next = head      
        # # make the _next the new head
        # head = _next
        # return head
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Exception :')
    print('[2,1,4,3]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1, 2, 3, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1]))))
    print()

    pass
# @lc main=end

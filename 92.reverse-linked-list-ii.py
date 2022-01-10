# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ Solution: Recursive """
        # successor = ListNode()

        # def reverseN(head, n):
        #     nonlocal successor
        #     if n == 1:
        #         successor = head.next
        #         return head
        #     last = reverseN(head.next, n-1)
        #     head.next.next = head
        #     head.next = successor
        #     return last
        # if left == 1:
        #     return reverseN(head, right)
        # head.next = self.reverseBetween(head.next, left-1, right-1)
        # return head
        """ Slution: Iterative """
        if not head:
            return None
        prev, curr = None, head

        while left > 1:
            prev, curr = curr, curr.next
            left -= 1
            right -= 1

        conn = prev
        tail = curr
        while right:
            curr.next, prev, curr = prev, curr, curr.next
            right -= 1

        # consider the case of node length is 1
        if conn:
            conn.next = prev
        else:
            head = prev
        tail.next = curr

        return head
        
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], left = 2, right = 4')
    print('Exception :')
    print('[1,4,3,2,5]')
    print('Output :')
    print(str(Solution().reverseBetween(
        listToListNode([1, 2, 3, 4, 5]), 2, 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [5], left = 1, right = 1')
    print('Exception :')
    print('[5]')
    print('Output :')
    print(str(Solution().reverseBetween(listToListNode([5]), 1, 1)))
    print()

    pass
# @lc main=end

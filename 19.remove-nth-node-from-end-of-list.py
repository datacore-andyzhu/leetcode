# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc tags=linked-list;two-pointers

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next

        # if fast travel n step already out of bound, we need
        # to return the head.next
        if fast is None:
            head = head.next
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], n = 2')
    print('Exception :')
    print('[1,2,3,5]')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1, 2, 3, 4, 5]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1], n = 1')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1]), 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1,2], n = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1, 2]), 1)))
    print()

    pass
# @lc main=end

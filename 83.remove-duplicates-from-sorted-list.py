# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Using the single pointer"""
        # curr = head

        # while curr:
        #     if curr.next and curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next

        # return head
        """Using two pointers"""
        # slow = head
        # fast = head
        # while fast:
        #     if fast.val != slow.val:
        #         slow.next = fast
        #         slow = slow.next
        #     fast = fast.next
        # if slow:
        #     slow.next = None
        # return head
        """ Solution 3 """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val==head.next.val else head

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 2]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,1,2,3,3]')
    print('Exception :')
    print('[1,2,3]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 2, 3, 3]))))
    print()

    pass
# @lc main=end

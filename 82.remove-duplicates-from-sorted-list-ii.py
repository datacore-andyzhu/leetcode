# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
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
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        while head:
            # we take care of the situation that head element is duplcated
            # skip all duplciate
            if head.next and head.val == head.next.val:
                # need to create a loop to find all duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all the duplicates
                prev.next = head.next
            # otherwise. move the prev pointer
            else:
                prev = prev.next
            # move forward
            head = head.next
        return dummyHead.next
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,3,4,4,5]')
    print('Exception :')
    print('[1,2,5]')
    print('Output :')
    print(str(Solution().deleteDuplicates(
        listToListNode([1, 2, 3, 3, 4, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,1,1,2,3]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 1, 2, 3]))))
    print()

    pass
# @lc main=end

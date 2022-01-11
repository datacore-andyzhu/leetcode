# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(next=head)

        smaller = ListNode(next=head)
        smaller_copy = smaller
        larger = ListNode(next=head)
        larger_copy = larger
        curr = dummy.next
        prev = None
        while curr:

            if curr.val < x:

                smaller_copy.next = curr
                smaller_copy = smaller_copy.next
            else:

                larger_copy.next = curr
                larger_copy = larger_copy.next
            prev = curr
            curr = curr.next
            prev.next = None
        larger_copy.next = None
        smaller_copy.next = larger.next
        return smaller.next
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,4,3,2,5,2], x = 3')
    print('Exception :')
    print('[1,2,2,4,3,5]')
    print('Output :')
    print(str(Solution().partition(listToListNode([1, 4, 3, 2, 5, 2]), 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [2,1], x = 2')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().partition(listToListNode([2, 1]), 2)))
    print()

    pass
# @lc main=end

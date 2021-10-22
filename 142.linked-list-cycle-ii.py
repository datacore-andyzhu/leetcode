# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return None
        # first identify if there is an cycle or not by using 2 pointers
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            # need to move the pointers first, then compare
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # break
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        if fast is None or fast.next is None:
            return None
        # slow = head

        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next

        # return slow
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [3,2,0,-4], pos = 1')
    print('Exception :')
    print('tail connects to node index 1')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([3, 2, 0, -4], pos=1))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2], pos = 0')
    print('Exception :')
    print('tail connects to node index 0')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([1, 2], pos=0))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1], pos = -1')
    print('Exception :')
    print('no cycle')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([1], pos=-1))))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
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
    def hasCycle(self, head: ListNode) -> bool:
        # either there is no node or there is only one node
        if head is None or head.next is None:
            return False
        # use slow and faster pointer to check
        # if there is a cycle, the faster and slow pointer will meet
        slow = head
        fast = head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        # using a set to record what we already seen
        # node_set = set()
        # while(head):
        #     if head in node_set:
        #         return True
        #     node_set.add(head)
        #     head = head.next
        # return False
        
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [3,2,0,-4], pos = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasCycle(listToListNode([3, 2, 0, -4], pos=1))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2], pos = 0')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasCycle(listToListNode([1, 2], pos=0))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1], pos = -1')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasCycle(listToListNode([1], pos=-1))))
    print()

    pass
# @lc main=end

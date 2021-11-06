# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1 = l1
        head_l2 = l2
        # Take care of the edge cases
        if head_l1 is None and head_l2 is not None:
            return l2
        if head_l2 is None and head_l1 is not None:
            return l1
        if head_l1 is None and head_l2 is None:
            return None

        # create a sentry node
        new_head = ListNode()
        current = new_head
        # go through each linked list
        while head_l1 and head_l2:
            if head_l1.val <= head_l2.val:
                current.next = head_l1
                head_l1 = head_l1.next
            else:
                current.next = head_l2
                head_l2 = head_l2.next

            current = current.next

        # is there are some left over on l1 or l2
        if head_l1:
            current.next = head_l1
        if head_l2:
            current.next = head_l2
        return new_head.next
        """ Solution 2: recursive """
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [1,2,4], l2 = [1,3,4]')
    print('Exception :')
    print('[1,1,2,3,4,4]')
    print('Output :')
    print(str(Solution().mergeTwoLists(
        listToListNode([1, 2, 4]), listToListNode([1, 3, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('l1 = [], l2 = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([]), listToListNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('l1 = [], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([]), listToListNode([0]))))
    print()

    pass
# @lc main=end

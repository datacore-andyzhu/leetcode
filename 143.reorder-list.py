# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """ Solution 1: use iterative method """
        # The overall solution is to first spli the linked list into two half
        # then reverse the second half
        # then merge the tow half

        # first identiy the 2nd half of the original list
        # we need to modify the original method a little bit
        # so the slow pointer will end up to teh node before the split
        slow = head
        fast = head.next  # soecial case in this problem
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow.next is point to the node that be split off
        second = slow.next
        slow.next = None  # the end of first half

        # start to reverse the 2nd half
        prev = None
        while second:
            second.next, second, prev = prev, second.next, second

        # now merge these two halfs, now the prev is new head
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2

        """ Solution 2: recursive somehow this method time out"""
    #     if head and head.next and head.next.next:
    #         head = self.helper(head)

    # def helper(self, node):
    #     if not node or not node.next or not node.next.next:
    #         return node
    #     prev = curr = node
    #     while curr.next:
    #         prev = curr
    #         curr = curr.next
    #     thirdNode = node.next
    #     node.next = curr
    #     prev.next = None
    #     curr.next = self.helper(thirdNode)
    #     return node


# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Exception :')
    print('[1,4,2,3]')
    print('Output :')
    print(str(Solution().reorderList(listToListNode([1, 2, 3, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[1,5,2,4,3]')
    print('Output :')
    print(str(Solution().reorderList(listToListNode([1, 2, 3, 4, 5]))))
    print()

    pass
# @lc main=end

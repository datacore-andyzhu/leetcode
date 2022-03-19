# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#


# @lc tags=Unknown

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
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        curr = head
        count = 0
        ans = 0
        while curr.next:
            num = curr.val
            ans = (ans + num) << 1
            curr = curr.next
        ans = ans + curr.val
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,0,1]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().getDecimalValue(listToListNode([1, 0, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [0]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().getDecimalValue(listToListNode([0]))))
    print()

    pass
# @lc main=end

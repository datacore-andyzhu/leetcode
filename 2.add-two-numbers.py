# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc tags=linked-list;math

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # even though the number is reversed represented in linked list,
        # this actually is exactly how we add two numbers, from 1 position
        # to ten's position, etc

        # create an sentinal node as the headnode of the new linked list
        dummyHead = ListNode()
        sumHead = dummyHead
        carry = 0
        # while l1 and l2 both has values
        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            sumHead.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            sumHead = sumHead.next
        while l1:
            val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            sumHead.next = ListNode(val)
            l1 = l1.next
            sumHead = sumHead.next
        while l2:
            val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            sumHead.next = ListNode(val)
            l2 = l2.next
            sumHead = sumHead.next
        # we should not forget that carry might be large than zero
        # we need to include this one as well
        if carry > 0:
            sumHead.next = ListNode(carry)
        return dummyHead.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[7,0,8]')
    print('Output :')
    print(str(Solution().addTwoNumbers(
        listToListNode([2, 4, 3]), listToListNode([5, 6, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('l1 = [0], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().addTwoNumbers(
        listToListNode([0]), listToListNode([0]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]')
    print('Exception :')
    print('[8,9,9,9,0,0,0,1]')
    print('Output :')
    print(str(Solution().addTwoNumbers(listToListNode(
        [9, 9, 9, 9, 9, 9, 9]), listToListNode([9, 9, 9, 9]))))
    print()

    pass
# @lc main=end

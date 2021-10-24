# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#


# @lc tags=ordered-map

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[3,4,5]')
    print('Output :')
    print(str(Solution().middleNode(listToListNode([1, 2, 3, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5,6]')
    print('Exception :')
    print('[4,5,6]')
    print('Output :')
    print(str(Solution().middleNode(listToListNode([1, 2, 3, 4, 5, 6]))))
    print()

    pass
# @lc main=end

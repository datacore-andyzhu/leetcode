# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def swap(node1, node2):
            node1.val, node2.val = node2.val, node1.val
        slow = head
        fast = head
        i = 1
        while i < k:
            fast = fast.next
            i += 1
        snap1 = fast
        while fast.next:
            slow = slow.next
            fast = fast.next

        swap(snap1, slow)

        return head
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 2')
    print('Exception :')
    print('[1,4,3,2,5]')
    print('Output :')
    print(str(Solution().swapNodes(listToListNode([1, 2, 3, 4, 5]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [7,9,6,6,7,8,3,0,9,5], k = 5')
    print('Exception :')
    print('[7,9,6,6,8,7,3,0,9,5]')
    print('Output :')
    print(str(Solution().swapNodes(
        listToListNode([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#


# @lc tags=linked-list

# @lc imports=start
from multiprocessing import dummy
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # """ Solution 1 """
        # if head is None:
        #     return None
        # current = head
        # previous = head
        # while current:
        #     if head.val == val:
        #         head = current.next
        #         current = head
        #         previous = head
        #         continue
        #     if current.val == val and current != previous:
        #         previous.next = current.next
        #     else:
        #         previous = current
        #     current = current.next
        # return head
        """ Solution 2 """
        # if not head:
        #     return None
        # dummy = ListNode(val=0, next=head)
        # curr = dummy
        # while curr.next:
        #     if curr.next.val == val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return dummy.next
        """ Solution 3 """
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,6,3,4,5,6], val = 6')
    print('Exception :')
    print('[1,2,3,4,5]')
    print('Output :')
    print(str(Solution().removeElements(
        listToListNode([1, 2, 6, 3, 4, 5, 6]), 6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [], val = 1')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().removeElements(listToListNode([]), 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [7,7,7,7], val = 7')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().removeElements(listToListNode([7, 7, 7, 7]), 7)))
    print()

    pass
# @lc main=end

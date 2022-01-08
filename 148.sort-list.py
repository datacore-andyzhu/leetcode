# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#


# @lc tags=linked-list;sort

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head):
            slow = head
            fast = head
            prev = None
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            return slow

        def merge(left, right):
            dummyHead = ListNode()
            tail = dummyHead

            while left is not None and right is not None:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                    tail = tail.next
                else:
                    tail.next = right
                    right = right.next
                    tail = tail.next
            tail.next = left if left is not None else right
            return dummyHead.next

        if not head or not head.next:
            return head
        mid = split(head)

        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,2,1,3]')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([4, 2, 1, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [-1,5,3,4,0]')
    print('Exception :')
    print('[-1,0,3,4,5]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([-1, 5, 3, 4, 0]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([]))))
    print()

    pass
# @lc main=end

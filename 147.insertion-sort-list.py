# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def insertNode(dummy, val):
            node = ListNode(val)
            if dummy.next is None:
                dummy.next = node

            elif node.val < dummy.next.val:
                node.next = dummy.next
                dummy.next = node
            else:
                curr = dummy.next
                prev = None
                while curr:
                    if node.val >= curr.val:
                        prev = curr
                        curr = curr.next
                    else:
                        break
                node.next = curr
                prev.next = node

        dummy = ListNode(0)
        while head:
            insertNode(dummy, head.val)
            head = head.next
        return dummy.next
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
    print(str(Solution().insertionSortList(listToListNode([4, 2, 1, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [-1,5,3,4,0]')
    print('Exception :')
    print('[-1,0,3,4,5]')
    print('Output :')
    print(str(Solution().insertionSortList(listToListNode([-1, 5, 3, 4, 0]))))
    print()

    pass
# @lc main=end

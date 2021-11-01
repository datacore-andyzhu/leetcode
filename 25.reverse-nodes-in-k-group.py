# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/hard/25.reverse-nodes-in-k-groups"""
        def reverse(head, tail, terminate):
            curr = head
            pre = None
            while curr != terminate:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            return tail, head
        dummyHead = ListNode()
        dummyHead.next = head
        pre = dummyHead

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummyHead.next
            next = tail.next
            head, tail = reverse(head, tail, tail.next)
            pre.next = head
            tail.next = next
            pre = tail
            head = next
        return dummyHead.next
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 2')
    print('Exception :')
    print('[2,1,4,3,5]')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 3')
    print('Exception :')
    print('[3,2,1,4,5]')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 1')
    print('Exception :')
    print('[1,2,3,4,5]')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('head = [1], k = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1]), 1)))
    print()

    pass
# @lc main=end

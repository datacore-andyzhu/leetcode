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
        """ Solution 1: """
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
        """ Solution: Recursive """
        # reverse between nodeA and nodeB
        def reverse(nodeA, nodeB):
            pre = None
            curr = nodeA
            nxt = nodeA
            while curr != nodeB:
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt
            return pre
        # main logic
        if head is None:
            return None
        a = b = head
        # determine reverse range 
        for i in range(k):
            if b is None:
                return head
            b = b.next

        newhead = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newhead

        """ Solution 2"""
        # def countLength(curr):
        #     count = 0
        #     while curr:
        #         curr = curr.next
        #         count += 1
        #     return count
        # def reverseBetween(head, m, n):
        #     dummyhead = ListNode(val=None, next=head)
        #     prev = dummyhead
        #     curr = head
        #     i = 1
        #     while i < m:
        #         prev, curr = curr, curr.next
        #         i += 1
        #     anchor = prev
        #     while i <= n:
        #         curr.next, prev, curr = prev, curr, curr.next
        #         i += 1
        #     anchor.next.next = curr
        #     anchor.next = prev
        #     return dummyhead.next
        # N = countLength(head)
        # i = 1
        # while i + k <= N+1:
        #     head = reverseBetween(head, i, i+k-1);
        #     i += k
        # return head

        """ Solution 3 """
        # def reverse(head, prev, count):
        #     while count > 0:
        #         nxt = head.next
        #         head.next = prev
        #         prev = head
        #         head = nxt
        #         count -= 1
        #     return prev
        # node = head
        # count = 0
        # while count < k:
        #     if node is None:
        #         return head
        #     node = node.next
        #     count += 1
        # prev = self.reverseKGroup(node, k)
        # return reverse(head, prev, k)

        """ Solution 4 """
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                curr.next, prev, curr = prev, curr, curr.next
                k -= 1
            return prev
        node = head
        count = 0
        while count < k:
            if node is None:
                return head
            node = node.next
            count += 1
        newhead = reverse(head, k)
        head.next = self.reverseKGroup(node, k)
        return newhead
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

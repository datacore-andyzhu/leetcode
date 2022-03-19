# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def getLength(curr):
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count

        length = getLength(head)
        per_list_length = length // k
        remainder = length % k
        res = []

        curr = head
        for _ in range(k):
            if remainder > 0:
                extra = 1
            else:
                extra = 0
            if curr:
                dummy = ListNode()
                ll = dummy
                for _ in range(per_list_length+extra):

                    if curr:
                        ll.next = curr
                        curr = curr.next
                        ll = ll.next
                    else:
                        ll = None
                if ll:
                    ll.next = None
                res.append(dummy.next)
            else:
                res.append(None)
            remainder -= 1
        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3], k = 5')
    print('Exception :')
    print('[[1],[2],[3],[],[]]')
    print('Output :')
    print(str(Solution().splitListToParts(listToListNode([1, 2, 3]), 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5,6,7,8,9,10], k = 3')
    print('Exception :')
    print('[[1,2,3,4],[5,6,7],[8,9,10]]')
    print('Output :')
    print(str(Solution().splitListToParts(
        listToListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)))
    print()

    pass
# @lc main=end

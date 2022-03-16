# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc tags=linked-list;divide-and-conquer;heap

# @lc imports=start

from imports import *
import collections
import heapq
import queue
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


import queue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Solution 1: Heap """
        # setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        # heap = []
        # head = ListNode()
        # curr = head
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heap.append((lists[i].val, i))
        # heapq.heapify(heap)

        # while heap:
        #     a, b = heapq.heappop(heap)
        #     curr.next = ListNode(a)
        #     curr = curr.next
        #     lists[b] = lists[b].next
        #     if lists[b]:
        #         heapq.heappush(heap, (lists[b].val, b))
        # return head.next
        """ Solution 2: Merge """
        # def merge2Lists(list1, list2):
        #     head = curr = ListNode(0)
        #     while list1 and list2:
        #         if list1.val <= list2.val:
        #             curr.next = list1
        #             list1 = list1.next
        #         else:
        #             curr.next = list2
        #             list2 = list2.next
        #         curr = curr.next
        #     if not list1:
        #         curr.next = list2
        #     else:
        #         curr.next = list1
        #     return head.next
        # amount = len(lists)
        # interval = 1
        # while interval < amount:
        #     for i in range(0, amount-interval, interval*2):
        #         lists[i] = merge2Lists(lists[i], lists[i+interval])
        #     interval *= 2
        # return lists[0] if amount > 0 else None
        """ SOlution 3: merge every 2 """
        def merge(l1, l2):
            if not l2:
                return l1
            if not l1:
                return l2
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        def partition(lists, start, end):
            if start == end:
                return lists[start]
            if start < end:
                mid = start + (end-start) // 2
                l1 = partition(lists, start, mid)
                l2 = partition(lists, mid+1, end)
                return merge(l1, l2)
            return None
        return partition(lists, 0, len(lists)-1)
                
# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('lists = [[1,4,5],[1,3,4],[2,6]]')
    print('Exception :')
    print('[1,1,2,3,4,4,5,6]')
    print('Output :')
    print(str(Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('lists = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().mergeKLists([])))
    print()

    print('Example 3:')
    print('Input : ')
    print('lists = [[]]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().mergeKLists([[]])))
    print()

    pass
# @lc main=end

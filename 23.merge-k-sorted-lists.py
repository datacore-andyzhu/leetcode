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


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # myHeap = [x for x in lists]
        # heapq.heapify(myHeap)
        # n = len(lists)
        # for _idx, _list in enumerate(lists):
        #     heapq.heappush(myHeap, {'arrayIndex': _idx,
        #                    'elementIndex': 0, 'value': -1 * _list.val})
        # result = []

        # while myHeap[0].value != float('inf'):
        #     top = heapq.heappop(myHeap)
        #     result.append(top.value)
        #     top.elementIndex += 1
        #     if top.elementIndex >= len(lists[top.arrayIndex]):
        #         top.value = float('inf')
        #     else:
        #         top.value = lists[top.arrayIndex][top.elementIndex]

        #     heapq.heapify(myHeap)

        # return result
        # create a min-heap using the first node of each list
        pq = queue.PriorityQueue()
        for x in lists:
            pq.put(x)

        # take two pointers, head and tail, where the head points to the first node
        # of the output list and tail points to its last node
        head = last = None

        # run till min-heap is empty
        while pq:

            # extract the minimum node from the min-heap
            min = pq.get()

            # add the minimum node to the output list
            if head is None:
                head = min
                last = min
            else:
                last.next = min
                last = min

            # take the next node from the "same" list and insert it into the min-heap
            if min.next:
                pq.put(min.next)

        # return head node of the merged list
        return head


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

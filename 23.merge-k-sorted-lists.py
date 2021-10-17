# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc tags=linked-list;divide-and-conquer;heap

# @lc imports=start
import collections
import heapq
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myHeap = heapq()
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('lists = [[1,4,5],[1,3,4],[2,6]]')
    print('Exception :')
    print('[1,1,2,3,4,4,5,6]')
    print('Output :')
    print(str(Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]])))
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
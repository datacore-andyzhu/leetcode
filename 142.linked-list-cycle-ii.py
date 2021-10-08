# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#


# @lc tags=linked-list;two-pointers

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [3,2,0,-4], pos = 1')
    print('Exception :')
    print('tail connects to node index 1')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([3,2,0,-4], pos = 1))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2], pos = 0')
    print('Exception :')
    print('tail connects to node index 0')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([1,2], pos = 0))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = [1], pos = -1')
    print('Exception :')
    print('no cycle')
    print('Output :')
    print(str(Solution().detectCycle(listToListNode([1], pos = -1))))
    print()
    
    pass
# @lc main=end
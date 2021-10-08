# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Exception :')
    print('[2,1,4,3]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1,2,3,4]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1]))))
    print()
    
    pass
# @lc main=end
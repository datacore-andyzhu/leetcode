# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#


# @lc tags=Unknown

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
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = 0
        dummy = ListNode(0, head)
        _map = defaultdict(ListNode)
        _map[0] = dummy
        curr = dummy
        while curr:
            prefix += curr.val
            _map[prefix] = curr
            curr = curr.next
        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val
            curr.next = _map[prefix].next
            curr = curr.next
        return dummy.next
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,-3,3,1]')
    print('Exception :')
    print('[3,1]')
    print('Output :')
    print(str(Solution().removeZeroSumSublists(listToListNode([1,2,-3,3,1]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,-3,4]')
    print('Exception :')
    print('[1,2,4]')
    print('Output :')
    print(str(Solution().removeZeroSumSublists(listToListNode([1,2,3,-3,4]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = [1,2,3,-3,-2]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().removeZeroSumSublists(listToListNode([1,2,3,-3,-2]))))
    print()
    
    pass
# @lc main=end
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        curr = head
        # curr.next is None, the cuu point to the last element of the linked list
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        if k % length != 0:
            k = k % length
            for i in range(length-k):
                curr = curr.next
        newhead = curr.next
        curr.next = None
        return newhead
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 2')
    print('Exception :')
    print('[4,5,1,2,3]')
    print('Output :')
    print(str(Solution().rotateRight(listToListNode([1,2,3,4,5]),2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [0,1,2], k = 4')
    print('Exception :')
    print('[2,0,1]')
    print('Output :')
    print(str(Solution().rotateRight(listToListNode([0,1,2]),4)))
    print()
    
    pass
# @lc main=end

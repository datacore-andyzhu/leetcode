# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        head1 = l1
        head2 = l2
        while head1:
            stack1.append(head1.val)
            head1 = head1.next
        while head2:
            stack2.append(head2.val)
            head2 = head2.next

        carry = 0
        res = None
        while stack1 or stack2 or carry != 0:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            curr_sum = val1 + val2 + carry
            node_val = curr_sum % 10
            curr = ListNode(node_val)
            carry = curr_sum // 10
            curr.next = res
            res = curr
        return res
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [7,2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[7,8,0,7]')
    print('Output :')
    print(str(Solution().addTwoNumbers(listToListNode([7,2,4,3]),listToListNode([5,6,4]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('l1 = [2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[8,0,7]')
    print('Output :')
    print(str(Solution().addTwoNumbers(listToListNode([2,4,3]),listToListNode([5,6,4]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('l1 = [0], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().addTwoNumbers(listToListNode([0]),listToListNode([0]))))
    print()
    
    pass
# @lc main=end

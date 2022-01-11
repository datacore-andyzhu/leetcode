# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Solution 1 """
#         if not head:
#             return None
#         switch = True
#         first = first_copy = ListNode(0)
#         second = second_copy = ListNode(0)
#         curr = head
#         while curr:
#             if switch:
#                 first_copy.next = curr
#                 first_copy = first_copy.next
#                 switch = not switch
#             else:
#                 second_copy.next = curr
#                 second_copy = second_copy.next
#                 switch = not switch
#             curr = curr.next

#         second_copy.next = None
#         first_copy.next = second.next
#         return first.next
        """ Solution 2 """
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
                
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[1,3,5,2,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([1,2,3,4,5]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [2,1,3,5,6,4,7]')
    print('Exception :')
    print('[2,3,6,7,1,5,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([2,1,3,5,6,4,7]))))
    print()
    
    pass
# @lc main=end

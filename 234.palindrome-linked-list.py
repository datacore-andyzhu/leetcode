# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """ Soluyion 1 """
        # val = []
        # curr = head
        # while curr:
        #     val.append(curr.val)
        #     curr = curr.next
        # return val == val[::-1]

        """ Solution 2 """
        def reverse(head):
            pre = None
            curr = nxt = head
            while curr is not None:
                nxt = curr.next
                curr.next = pre
                pre = curr

                curr = nxt
            return pre
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        left = head
        right = reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome(listToListNode([1,2,2,1]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome(listToListNode([1,2]))))
    print()
    
    pass
# @lc main=end

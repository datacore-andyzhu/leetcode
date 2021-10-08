# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # """option 1 use recursive method"""
        # # clear out the edge case: empty linked list
        # if head is None:
        #     return None
        # # start the resursive algorithm, set the base case
        # if head.next is None:
        #     return head
        # last = self.reverseList(head.next)
        # # after recursive rest if the node, set the head.next element point back 
        # # to the head element
        # head.next.next = head
        # # set head.next to None
        # head.next = None
        # return last
        """ Option 2: Iterative method """
        curr = head
        prev = None
        while curr:
            # save the next element to a temp
            temp = curr.next
            # reverse the next link
            curr.next = prev 
            prev = curr
            curr = temp
        # at the end, curr point to the initial linked list last element's next poistion
        return prev
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[5,4,3,2,1]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([1, 2, 3, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([1, 2]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([]))))
    print()

    pass
# @lc main=end

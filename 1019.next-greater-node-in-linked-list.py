# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#


# @lc tags=array;two-pointers

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
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        stack_loc = []
        loc = -1
        res = []
        while head:
            loc += 1
            res.append(0)
            while stack and stack[-1] < head.val:
                res[stack_loc[-1]] = head.val
                stack.pop()
                stack_loc.pop()
            stack.append(head.val)
            stack_loc.append(loc)
            head = head.next
        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [2,1,5]')
    print('Exception :')
    print('[5,5,0]')
    print('Output :')
    print(str(Solution().nextLargerNodes(listToListNode([2, 1, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [2,7,4,3,5]')
    print('Exception :')
    print('[7,0,5,5,0]')
    print('Output :')
    print(str(Solution().nextLargerNodes(listToListNode([2, 7, 4, 3, 5]))))
    print()

    pass
# @lc main=end

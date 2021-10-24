# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        if p1 is not None:
            return p1
        else:
            return None
        

        
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =2, skipB = 3')
    print('Exception :')
    print('Intersected at '8'')
    print('Output :')
    print(str(Solution().getIntersectionNode(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,skipB = 1')
    print('Exception :')
    print('Intersected at '2'')
    print('Output :')
    print(str(Solution().getIntersectionNode(error, error)))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2')
    print('Exception :')
    print('No intersection')
    print('Output :')
    print(str(Solution().getIntersectionNode(error, error)))
    print()

    pass
# @lc main=end

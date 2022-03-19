# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#


# @lc tags=hash-table;design

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
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """ solution 1 """
        nums = set(nums)
        res = 0
        prevInNums = False

        while head:
            if head.val in nums:
                if not prevInNums:
                    prevInNums = True
                    res += 1
            else:
                prevInNums = False

            head = head.next

        return res

        """ Solution 2 """
        nums = set(nums)
        res = 0
        while head:
            if head.val in nums and (head.next is None or head.next.val not in nums):
                res += 1
            head = head.next

        return res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [0,1,2,3], nums = [0,1,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numComponents(
        listToListNode([0, 1, 2, 3]), [0, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [0,1,2,3,4], nums = [0,3,1,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numComponents(
        listToListNode([0, 1, 2, 3, 4]), [0, 3, 1, 4])))
    print()

    pass
# @lc main=end

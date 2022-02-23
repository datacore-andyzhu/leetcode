# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#


# @lc tags=reservoir-sampling

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

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        curr = head
        self.count = 0
        while curr:
            self.count += 1
            curr = curr.next

    def getRandom(self) -> int:
        # i = 0
        # result = self.head.val
        # current = self.head

        # while current:
        #     i += 1
        #     if random.randint(0, i) == 0:
        #         result = current.val
        #     current = current.next
        # return result
        curr = self.head
        r = random.randint(1,self.count)
        for i in range(1,r):
            curr = curr.next
        return curr.val
    """ Solution 2: reservior sampling """

    def __init__(self, head) -> None:
        self.head = head
    
    def getRandom(self) -> int:
        chosen = 0
        scope = 1
        curr = self.head
        while curr:
            if random.random() < 1/scope:
                chosen = curr.val
            curr = curr.next
            scope += 1
        return chosen
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end

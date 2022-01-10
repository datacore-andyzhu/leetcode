# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#


# @lc tags=linked-list;depth-first-search

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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """ Solution 1: """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        prev.next = None
        headright = slow.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(headright)

        return root

        """ Solution 2: binary with in order traversal """
        def getSize(head):
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count

        def convert(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l+r) // 2
            left = convert(l, mid-1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid+1, r)
            return node
        size = getSize(head)
        return convert(0, size-1)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [-10,-3,0,5,9]')
    print('Exception :')
    print('[0,-3,9,-10,null,5]')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([-10, -3, 0, 5, 9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([]))))
    print()

    pass
# @lc main=end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            if not node:
                return None
            prev = None
            curr = node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next

            return prev

        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        tail = reverse(slow)
        max_value = 0
        curr = head
        while tail:
            max_value = max(max_value, curr.val + tail.val)
            curr = curr.next
            tail = tail.next
        return max_value

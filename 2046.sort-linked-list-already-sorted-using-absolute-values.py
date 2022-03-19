
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0, head)

        prev = dummyhead
        curr = head
        while curr:
            if curr.val < 0 and prev is not dummyhead:

                prev.next = curr.next
                curr.next = dummyhead.next
                dummyhead.next = curr
                curr = prev.next
            else:
                prev, curr = curr, curr.next
        return dummyhead.next

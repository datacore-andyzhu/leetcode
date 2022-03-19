# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        nums_dict = defaultdict(int)
        curr = head
        while curr:
            nums_dict[curr.val] += 1
            curr = curr.next

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if nums_dict[curr.val] > 1:
                prev.next = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next

        return dummy.next

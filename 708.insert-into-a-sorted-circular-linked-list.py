"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev, curr = head, head.next
        need_insert = False
        while True:
            # insert number is between some nodes
            if prev.val <= insertVal <= curr.val:
                need_insert = True
            # insert number is between head and tail of the list
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    need_insert = True
            if need_insert:
                prev.next = Node(insertVal, curr)
                return head
            prev, curr = curr, curr.next

            # come back to once full cycle
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head

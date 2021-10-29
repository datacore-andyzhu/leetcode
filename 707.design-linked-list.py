# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#


# @lc tags=Unknown

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


class ListNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size-1:
            return -1
        head = self.head
        for i in range(index):
            head = head.next
        return head.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
        return 

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            return self.addAtHead(val)
        head = self.head
        while head.next:
            head = head.next
        new_node = ListNode(val)
        head.next = new_node
        new_node.next = None
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)

        curr = self.head
        for i in range(1, index):
            curr = curr.next
        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size-1:
            return -1
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        prev = self.head
        curr = self.head.next
        for i in range(1, index):
            prev = curr
            curr = curr.next
        if curr.next is None:
            prev.next = None
            self.size -= 1
        else:
            prev.next = curr.next
            self.size -= 1

        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end

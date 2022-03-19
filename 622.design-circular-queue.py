# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
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
class MyCircularQueue:
    """ Solution 1 """
    # def __init__(self, k: int):
    #     self.head = 0
    #     self.tail = 0
    #     self.capacity = k+1
    #     self.queue = [None] * (k+1)


    # def enQueue(self, value: int) -> bool:
    #     if self.isFull():
    #         return False
    #     self.queue[self.tail] = value
    #     self.tail = (self.tail + 1) % self.capacity
    #     return True
        

    # def deQueue(self) -> bool:
    #     if self.isEmpty():
    #         return False
    #     self.head = (self.head + 1) % self.capacity
    #     return True

    # def Front(self) -> int:
    #     if self.isEmpty():
    #         return -1
    #     return self.queue[self.head]

    # def Rear(self) -> int:
    #     if self.isEmpty():
    #         return -1
    #     # 当 tail 为 0 时防止数组越界
    #     return self.queue[((self.tail-1)+self.capacity)%self.capacity]
        

    # def isEmpty(self) -> bool:
    #     return self.head == self.tail 

    # def isFull(self) -> bool:
    #     return self.head == (self.tail + 1) % self.capacity
        
    """ Solution 2 """

    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.capacity = k
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1        
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return self.head == (self.tail + 1) % self.capacity

    """ Solution 3 """


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
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
    print(str(Solution().__init__(error)))
    print()
    
    pass
# @lc main=end

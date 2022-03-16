""" Solution 1: Double linkedlist + heapq """
import heapq
import collections

class DoubleLinkedList:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def connect(self, other):
        self.next = other
        other.prev = self

    def insert(self, other):
        next_node = self.next
        self.connect(other)
        other.connect(next_node)

    def remove(self):
        self.prev.connect(self.next)


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head, self.tail = DoubleLinkedList(), DoubleLinkedList()
        self.head.connect(self.tail)
        self.val2nodes = collections.defaultdict(list)
        self.max_heap = []

    def push(self, x: int) -> None:
        node = DoubleLinkedList(x)
        # insert into doubly linked list
        self.tail.prev.insert(node)
        # update dict
        self.val2nodes[x].append(node)
        # insert into heap
        heapq.heappush(self.max_heap, -x)  # O(logN)

    def pop(self) -> int:
        node = self.tail.prev
        # remove from doubly linked list
        self.tail.prev.remove()
        # update dict
        val = node.val
        self.val2nodes[val].pop()
        if not self.val2nodes[val]:
            del self.val2nodes[val]
        # note: we do not remove that element in heap here, instead, do the deletion during peekMax based on the dict
        # if we use TreeMap in java here for clean up, remove that val will cost logN time only
        return val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        # operate the deletion here
        while -self.max_heap[0] not in self.val2nodes:
            heapq.heappop(self.max_heap)

        return -self.max_heap[0]

    def popMax(self) -> int:
        max_val = self.peekMax()  # avg: logN
        # update heap
        heapq.heappop(self.max_heap)  # logN
        # update dict
        node = self.val2nodes[max_val].pop()
        if not self.val2nodes[max_val]:
            del self.val2nodes[max_val]
        # update doubly linked list
        node.remove()

        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

""" Solution 2: two stacks """


class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        max_in_stack = self.maxStack[-1] if len(self.maxStack) != 0 else x
        if max_in_stack > x:
            self.maxStack.append(max_in_stack)
        else:
            self.maxStack.append(x)
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            self.maxStack.pop()
            return self.stack.pop()

        return -1

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        max_in_stack = self.peekMax()
        buffer = []
        while self.top() != max_in_stack:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_in_stack


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

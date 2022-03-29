class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class PhoneDirectory:

#     def __init__(self, maxNumbers: int):
#         self.queue = [i for i in range(maxNumbers)]
#         self.s = set(self.queue)


#     def get(self) -> int:
#         if self.queue:
#             ans = self.queue.pop(0)
#             self.s.remove(ans)
#             return ans
#         else:
#             return -1

#     def check(self, number: int) -> bool:
#         return number in self.s

#     def release(self, number: int) -> None:
#         if number not in self.s:
#             self.s.add(number)
#             self.queue.append(number)

class PhoneDirectory:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.head = None
        self.hsh = {val: True for val in range(maxNumbers)}
        for val in reversed(range(maxNumbers)):
            node = Node(val)
            node.next = self.head
            self.head = node

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.head:
            return -1
        number = self.head.val
        self.hsh[number] = False
        self.head = self.head.next
        return number

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.hsh and self.hsh[number]

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if self.check(number):
            return
        node = Node(number)
        node.next = self.head
        self.head = node
        self.hsh[number] = True

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#


# @lc tags=design

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
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, other):
        other.next , other.prev = None, None
        if self.head == None:
            self.head = other
        else:
            self.tail.next = other
            other.prev = self.tail
        self.tail = other
    
    def delete(self, other):
        if other.prev:
            other.prev.next = other.next
        else:
            self.head = other.next

        if other.next:
            other.next.prev = other.prev
        else:
            self.tail = other.prev
        other.next, other.prev = None, None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_to_node = defaultdict(LinkedList)
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        old_node = self.key_to_node[key]
        self.key_to_node[key] = ListNode(key, old_node.val, old_node.freq)
        self.freq_to_node[old_node.freq].delete(old_node)
        if not self.freq_to_node[self.key_to_node[key].freq].head:
            del self.freq_to_node[self.key_to_node[key].freq]
            if self.min_freq == self.key_to_node[key].freq:
                self.min_freq += 1
        self.key_to_node[key].freq += 1
        self.freq_to_node[self.key_to_node[key].freq].append(self.key_to_node[key])

        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if self.get(key) != -1:
            self.key_to_node[key].val = value
            return
        if self.size == self.capacity:
            del self.key_to_node[self.freq_to_node[self.min_freq].head.key]
            self.freq_to_node[self.min_freq].delete(self.freq_to_node[self.min_freq].head)
            if not self.freq_to_node[self.min_freq].head:
                del self.freq_to_node[self.min_freq]
            self.size -= 1
        self.min_freq = 1
        self.key_to_node[key] = ListNode(key, value, self.min_freq)
        self.freq_to_node[self.key_to_node[key].freq].append(self.key_to_node[key])
        self.size += 1
    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
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
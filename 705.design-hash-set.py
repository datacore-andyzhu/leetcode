# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
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
class MyHashSet:

    def __init__(self):
        self.arr = [None] * 8
        self.capacity = 8
        self.size = 0
        self.threshold = 2/3

    def hash(self, key):
        return key % self.capacity

    def rehash(self, key):
        return (5*key + 1) % self.capacity

    def insertPos(self, key):
        pos = self.hash(key)
        # use -1 to represent teh 'removed' item
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                return -1
            if self.arr[pos] == -1:
                break
            pos = self.rehash(pos)
        return pos

    def safeAdd(self, key):
        pos = self.insertPos(key)
        # already in
        if pos == -1:
            return
        self.arr[pos] = key
        self.size += 1

    def safeAddArr(self, arr):
        for val in arr:
            if val is not None:
                self.safeAdd(val)

    def add(self, key: int) -> None:
        def preAdd(self):
            if self.size / self.capacity <= self.threshold:
                return
            self.capacity <<= 1
            oldArr, self.arr = copy.deepcopy(self.arr), [None] * self.capacity
            self.safeAddArr(oldArr)
        preAdd(self)
        self.safeAdd(key)

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                self.arr[pos] = -1
                self.size -= 1
                return
            pos = self.rehash(pos)
        return

    def contains(self, key: int) -> bool:
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                return True
            pos = self.rehash(pos)
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
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

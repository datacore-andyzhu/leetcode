# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
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


class MyHashMap:

    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
        else:
            self.hashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]
        else:
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

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

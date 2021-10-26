# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc tags=stack;design

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


class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if self.minStack == [] or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # value = self.mainStack.pop()
        # if value == self.minStack[-1]:
        #     self.minStack.pop()
        if self.mainStack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

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

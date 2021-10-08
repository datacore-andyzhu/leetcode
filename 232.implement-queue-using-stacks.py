# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
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
class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back = []
        self.front.append(x)
        self.back = self.front[::-1]

    def pop(self) -> int:
        self.front = []
        item = self.back.pop()
        self.front = self.back[::-1]
        return item

    def peek(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        return self.front == []

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
       
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
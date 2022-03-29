# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#


# @lc tags=heap;breadth-first-search

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


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]
        self.freq_stack[self.freq[val]].append(val)

    def pop(self) -> int:
        ans = self.freq_stack[self.max_freq].pop()
        self.freq[ans] -= 1
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
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

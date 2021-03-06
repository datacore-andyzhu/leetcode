# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#


# @lc tags=reservoir-sampling

# @lc imports=start
import collections
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
class Solution:
    """ Solution 1 """
    def __init__(self, nums: List[int]):
        self.numCounter = {}
        for i in range(len(nums)):
            if self.numCounter.get(nums[i], -1) == -1:
                self.numCounter[nums[i]] = [i]
            else:
                self.numCounter[nums[i]].append(i)
        

        

    def pick(self, target: int) -> int:
        
        self.rand = random.randrange(len(self.numCounter[target]))
        return self.numCounter[target][self.rand]

    """ Solution 2: Reservior Sampling """

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        n = len(self.nums)
        count = 0
        idx = 0
        for i in range(n):
            if self.nums[i] == target:
                count += 1
                # the randint should choose from 1 to count, not 0 to count
                # 0...count mean sample size is count+1
                if random.randint(1, count) == 1:
                    idx = i
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
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

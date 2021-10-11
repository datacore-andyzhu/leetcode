# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#


# @lc tags=dynamic-programming

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


class NumArray:

    def __init__(self, nums: List[int]):
        self.numSum = [0]*(len(nums)+1)
        for i in range(1, len(self.numSum)):
            self.numSum[i] = self.numSum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.numSum[right+1] - self.numSum[left]

    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

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

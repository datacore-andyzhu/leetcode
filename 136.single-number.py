# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc tags=hash-table;bit-manipulation

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
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 
        for num in nums:
            result = result ^ num
        return result
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,2,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().singleNumber([2,2,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [4,1,2,1,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().singleNumber([4,1,2,1,2])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().singleNumber([1])))
    print()
    
    pass
# @lc main=end
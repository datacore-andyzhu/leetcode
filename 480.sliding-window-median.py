# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#


# @lc tags=sliding-window

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
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,-1,-3,5,3,6,7], k = 3')
    print('Exception :')
    print('[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]')
    print('Output :')
    print(str(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,2,3,1,4,2], k = 3')
    print('Exception :')
    print('[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]')
    print('Output :')
    print(str(Solution().medianSlidingWindow([1,2,3,4,2,3,1,4,2],3)))
    print()
    
    pass
# @lc main=end
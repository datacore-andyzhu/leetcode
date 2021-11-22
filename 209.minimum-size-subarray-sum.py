# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc tags=array;two-pointers;binary-search

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
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        right = 0
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            while left <= right and curr_sum >= target:
                min_length = min(min_length, right-left+1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float('inf') else 0
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('target = 7, nums = [2,3,1,2,4,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minSubArrayLen(7,[2,3,1,2,4,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('target = 4, nums = [1,4,4]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSubArrayLen(4,[1,4,4])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('target = 11, nums = [1,1,1,1,1,1,1,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minSubArrayLen(11,[1,1,1,1,1,1,1,1])))
    print()
    
    pass
# @lc main=end
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc tags=array;two-pointers

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
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            _height = min(height[left], height[right])
            _width = right - left
            max_area = max(max_area, _height * _width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [1,8,6,2,5,4,8,3,7]')
    print('Exception :')
    print('49')
    print('Output :')
    print(str(Solution().maxArea([1,8,6,2,5,4,8,3,7])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('height = [1,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxArea([1,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('height = [4,3,2,1,4]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().maxArea([4,3,2,1,4])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('height = [1,2,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxArea([1,2,1])))
    print()
    
    pass
# @lc main=end
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc tags=array;two-pointers;stack

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
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        leftMax = [0] * size
        rightMax = [0] * size
        leftMax[0] = height[0]
        for i in range(1, size):
            leftMax[i] = max(leftMax[i-1], height[i])
        rightMax[size-1] = height[size-1]
        for j in range(size-2, -1, -1):
            rightMax[j] = max(rightMax[j+1], height[j])

        for k in range(1, size-1):
            ans += min(leftMax[k], rightMax[k]) - height[k]

        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [0,1,0,2,1,0,1,3,2,1,2,1]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('height = [4,2,0,3,2,5]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().trap([4, 2, 0, 3, 2, 5])))
    print()

    pass
# @lc main=end

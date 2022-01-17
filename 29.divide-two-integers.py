# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc tags=math;binary-search

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
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        x = dividend
        y = divisor
        negative = False
        if (x > 0 and y < 0) or (x < 0 and y > 0):
            negative = True

        if x < 0:
            x = -x
        if y < 0:
            y = -y

        def mul(a, k):
            ans = 0
            while k > 0:
                if (k & 1) == 1:
                    ans += a
                k >>= 1
                a += a
            return ans

        left = 0
        right = x
        while left < right:
            mid = (left + right + 1) >> 1
            if mul(mid, y) <= x:
                left = mid
            else:
                right = mid - 1

        ans = -left if negative else left
        if ans > INT_MAX or ans < INT_MIN:
            return INT_MAX
        return int(ans)

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('dividend = 10, divisor = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().divide(10,3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('dividend = 7, divisor = -3')
    print('Exception :')
    print('-2')
    print('Output :')
    print(str(Solution().divide(7,-3)))
    print()
    
    pass
# @lc main=end

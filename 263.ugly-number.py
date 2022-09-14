# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#


# @lc tags=math

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
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 6')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isUgly(6)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isUgly(1)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 14')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isUgly(14)))
    print()
    
    pass
# @lc main=end

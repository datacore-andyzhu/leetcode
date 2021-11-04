# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lc tags=math;bit-manipulation

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
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n-1) == 0
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 16')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(16)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfTwo(3)))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(4)))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfTwo(5)))
    print()
    
    pass
# @lc main=end
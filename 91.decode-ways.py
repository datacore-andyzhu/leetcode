# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc tags=string;dynamic-programming

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
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        # string with zero length has 0 ways to decode
        dp[0] = 1
        # for string length of 1, depends on if it is '0' or non '0'
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2, len(s)+1):
            singleDigit = int(s[i-1])
            twoDigits = int(s[i-2:i])
            if singleDigit >= 1:
                dp[i] += dp[i-1]
            if 10 <= twoDigits <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "12"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numDecodings("12")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "226"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numDecodings("226")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "06"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numDecodings("06")))
    print()
    
    pass
# @lc main=end

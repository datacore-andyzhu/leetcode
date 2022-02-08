# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lc tags=string;dynamic-programming;backtracking;greedy

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
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False for j in range(n + 1)] for i in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    if s[i - 1] == p[j - 1] or p[j-1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aa", p = "a"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isMatch("aa","a")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "aa", p = "*"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("aa","*")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "cb", p = "?a"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isMatch("cb","?a")))
    print()
    
    pass
# @lc main=end

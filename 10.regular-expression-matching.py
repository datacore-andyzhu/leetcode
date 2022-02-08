# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc tags=string;dynamic-programming;backtracking

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
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] | dp[i-1][j]

                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
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
    print('s = "aa", p = "a*"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("aa","a*")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "ab", p = ".*"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("ab",".*")))
    print()
    
    pass
# @lc main=end

# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc tags=binary-search;dynamic-programming;greedy

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
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[m][n] == m:
            return True
        return False
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abc", t = "ahbgdc"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSubsequence("abc", "ahbgdc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "axc", t = "ahbgdc"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSubsequence("axc", "ahbgdc")))
    print()

    pass
# @lc main=end

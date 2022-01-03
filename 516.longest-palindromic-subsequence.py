# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#


# @lc tags=dynamic-programming

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
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "bbbab"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestPalindromeSubseq("bbbab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cbbd"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().longestPalindromeSubseq("cbbd")))
    print()

    pass
# @lc main=end

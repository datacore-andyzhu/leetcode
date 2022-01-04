# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc tags=Unknown

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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('text1 = "abcde", text2 = "ace"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().longestCommonSubsequence("abcde","ace")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('text1 = "abc", text2 = "abc"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().longestCommonSubsequence("abc","abc")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('text1 = "abc", text2 = "def"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().longestCommonSubsequence("abc","def")))
    print()
    
    pass
# @lc main=end

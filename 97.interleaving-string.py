# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if(len1+len2 != len3):
            return False
        dp = [[False]*(len2+1) for i in range(len1+1)]
        dp[0][0] = True
        for i in range(1, len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
        for i in range(1, len2+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]
                            ) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s1 = "", s2 = "", s3 = ""')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isInterleave("", "", "")))
    print()

    pass
# @lc main=end

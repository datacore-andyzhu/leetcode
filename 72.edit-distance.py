# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
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
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[-1][-1]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('word1 = "horse", word2 = "ros"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minDistance("horse","ros")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('word1 = "intention", word2 = "execution"')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().minDistance("intention","execution")))
    print()
    
    pass
# @lc main=end

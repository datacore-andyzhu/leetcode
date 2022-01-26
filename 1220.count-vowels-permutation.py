# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
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
    def countVowelPermutation(self, n: int) -> int:
        # originally each letter can transition to any other vowels
        # including itself
        # first draw the transition graph, then
        # use the condition in problem to eliminate the impossible ones
        # then we get
        # 'a' can be transition from 'e', 'u', 'i'
        # 'e' can be transition from 'a', 'i'
        # 'i' can be transition from 'e', 'o'
        # 'o' can be transition from 'i'
        # 'u' can be transition from 'i', 'o'
        # we could use dp[i][j] to record ith char with jth voewl
        # j range from 0 ~ 4 to represent 'a', 'e', 'i', 'o', 'u'
        # but we can simply the dp table to only one array
        # like the following
        # dp[0] -> 'a'
        # dp[1] -> 'e'
        # dp[2] -> 'i'
        # dp[3] -> 'o'
        # dp[4] -> 'u'
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007,
                  (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().countVowelPermutation(1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().countVowelPermutation(2)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('68')
    print('Output :')
    print(str(Solution().countVowelPermutation(5)))
    print()
    
    pass
# @lc main=end

# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "leetcode", wordDict = ["leet","code"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordBreak("leetcode", ["leet", "code"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "applepenapple", wordDict = ["apple","pen"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordBreak("applepenapple", ["apple", "pen"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordBreak("catsandog", [
          "cats", "dog", "sand", "and", "cat"])))
    print()

    pass
# @lc main=end

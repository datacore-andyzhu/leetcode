# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
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
    """ Solution 1 """
    # def isPalindrome(self, s, left, right):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return s[left+1:right]

    # def longestPalindrome(self, s: str) -> str:
    #     # this function starts in the middle of string
    #     # going left and right and verify left char and right char are
    #     # equal

    #     n = len(s)
    #     result = ''
    #     for i in range(n):
    #         # because we do not know starting in position i
    #         # as middle of the string, the string length is odd or even

    #         s1 = self.isPalindrome(s, i, i)
    #         s2 = self.isPalindrome(s, i, i+1)
    #         result = s1 if len(s1) > len(result) else result
    #         result = s2 if len(s2) > len(result) else result
    #     return result
    """ Solution 2: DP """

    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        maxLength = 0
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True
                if dp[i][j] and j-i+1 > maxLength:
                    maxLength = j-i+1
                    left = i
                    right = j

        return s[left:right+1]

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "babad"')
    print('Exception :')
    print('"bab"')
    print('Output :')
    print(str(Solution().longestPalindrome("babad")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cbbd"')
    print('Exception :')
    print('"bb"')
    print('Output :')
    print(str(Solution().longestPalindrome("cbbd")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().longestPalindrome("a")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "ac"')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().longestPalindrome("ac")))
    print()

    pass
# @lc main=end

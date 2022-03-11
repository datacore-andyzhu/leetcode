# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


# @lc tags=string

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
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return checkPalindrome(s, start+1, end) or checkPalindrome(s, start, end-1)
        return True
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aba"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validPalindrome("aba")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abca"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validPalindrome("abca")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "abc"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validPalindrome("abc")))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc tags=two-pointers;string

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
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
        return True
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "A man, a plan, a canal: Panama"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome("A man, a plan, a canal: Panama")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "race a car"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome("race a car")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = " "')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome(" ")))
    print()

    pass
# @lc main=end

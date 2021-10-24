# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc tags=math

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
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        reverse_number = 0
        old_number = x
        while old_number > 0:
            remainder = old_number % 10
            reverse_number = reverse_number * 10 + remainder
            old_number = old_number // 10
        if x == reverse_number:
            return True
        else:
            return False

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 121')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome(121)))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = -121')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome(-121)))
    print()

    print('Example 3:')
    print('Input : ')
    print('x = 10')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome(10)))
    print()

    print('Example 4:')
    print('Input : ')
    print('x = -101')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome(-101)))
    print()

    pass
# @lc main=end

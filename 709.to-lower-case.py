# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
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
    def toLowerCase(self, s: str) -> str:

        return s.lower()

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Hello"')
    print('Exception :')
    print('"hello"')
    print('Output :')
    print(str(Solution().toLowerCase("Hello")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "here"')
    print('Exception :')
    print('"here"')
    print('Output :')
    print(str(Solution().toLowerCase("here")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "LOVELY"')
    print('Exception :')
    print('"lovely"')
    print('Output :')
    print(str(Solution().toLowerCase("LOVELY")))
    print()

    pass
# @lc main=end

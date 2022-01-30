# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
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
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            columnNumber -= 1
            # print((columnNumber % 26 - 1))
            s = chr(ord('A') + (columnNumber % 26)) + s
            columnNumber = columnNumber // 26
        return s
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('columnNumber = 1')
    print('Exception :')
    print('"A"')
    print('Output :')
    print(str(Solution().convertToTitle(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('columnNumber = 28')
    print('Exception :')
    print('"AB"')
    print('Output :')
    print(str(Solution().convertToTitle(28)))
    print()

    print('Example 3:')
    print('Input : ')
    print('columnNumber = 701')
    print('Exception :')
    print('"ZY"')
    print('Output :')
    print(str(Solution().convertToTitle(701)))
    print()

    pass
# @lc main=end

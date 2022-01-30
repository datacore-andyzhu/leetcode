# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
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
    def titleToNumber(self, columnTitle: str) -> int:
        # return sum([(ord(columnTitle[i]) - ord('A') + 1)*26**(len(columnTitle)-i-1) for i in range(len(columnTitle))])
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[i]) -
                       ord('A') + 1)*26**(len(columnTitle)-i-1)
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('columnTitle = "A"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().titleToNumber("A")))
    print()

    print('Example 2:')
    print('Input : ')
    print('columnTitle = "AB"')
    print('Exception :')
    print('28')
    print('Output :')
    print(str(Solution().titleToNumber("AB")))
    print()

    print('Example 3:')
    print('Input : ')
    print('columnTitle = "ZY"')
    print('Exception :')
    print('701')
    print('Output :')
    print(str(Solution().titleToNumber("ZY")))
    print()

    pass
# @lc main=end

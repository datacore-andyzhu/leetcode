# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
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
    def convert(self, s: str, numRows: int) -> str:
        """ Solution 1 """
#         if numRows == 1:
#             return s
#         n = len(s)
#         cycle = 2*numRows - 2
#         strlist = []
#         for i in range(numRows):
#             for j in range(i, n, cycle):
#                 strlist.append(s[j])
#                 if i != numRows - 1 and i != 0 and j+cycle-2*i < n:
#                     strlist.append(s[j+cycle-2*i])
#         result = ''.join(strlist)

        # return result
        """ Solution 2 """
        if numRows == 1:
            return s
        n = len(s)
        change = False
        rows = min(n, numRows)
        strlist = [[] for _ in range(rows)]
        print(strlist)
        row = 0
        for i in range(n):
            strlist[row].append(s[i])
            if row == rows-1 or row == 0:
                change = not change
            row = row + 1 if change else row - 1
        result = ''
        for j in range(rows):
            result += ''.join(strlist[j])
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "PAYPALISHIRING", numRows = 3')
    print('Exception :')
    print('"PAHNAPLSIIGYIR"')
    print('Output :')
    print(str(Solution().convert("PAYPALISHIRING", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "PAYPALISHIRING", numRows = 4')
    print('Exception :')
    print('"PINALSIGYAHRPI"')
    print('Output :')
    print(str(Solution().convert("PAYPALISHIRING", 4)))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "A", numRows = 1')
    print('Exception :')
    print('"A"')
    print('Output :')
    print(str(Solution().convert("A", 1)))
    print()

    pass
# @lc main=end

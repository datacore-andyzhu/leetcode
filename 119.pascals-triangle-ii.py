# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#


# @lc tags=array

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
    def getRow(self, rowIndex: int) -> List[int]:
        """ Option 1: Iterative """
        # pascalTriangle = []
        # trow = [1]
        # y = [0]
        # if rowIndex == 0:
        #     return trow

        # for i in range(rowIndex):
        #     pascalTriangle.append(trow)
        #     trow = [l+r for l, r in zip(trow+y, y+trow)]
        # return trow

        """ Option 2: Recursive """
        def getNum(row, col, memo):
            if memo[row][col] != None:
                return memo[row][col]
            if row == 0 or col == 0 or row==col:
                return 1
            
            res = getNum(row-1, col-1, memo) + getNum(row-1, col, memo)
            memo[row][col] = res
            return res
        
        result = []
        memo = [[None for _ in range(rowIndex+1)] for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            result.append(getNum(rowIndex, i, memo))
        
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rowIndex = 3')
    print('Exception :')
    print('[1,3,3,1]')
    print('Output :')
    print(str(Solution().getRow(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('rowIndex = 0')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().getRow(0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('rowIndex = 1')
    print('Exception :')
    print('[1,1]')
    print('Output :')
    print(str(Solution().getRow(1)))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        mx = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    dp[i][j] = 1
                else:

                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1]
                                       [j], dp[i][j-1]) + 1
                mx = max(mx, dp[i][j])
        return mx*mx
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maximalSquare([["1", "0", "1", "0", "0"], [
          "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [["0","1"],["1","0"]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maximalSquare([["0", "1"], ["1", "0"]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [["0"]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maximalSquare([["0"]])))
    print()

    pass
# @lc main=end

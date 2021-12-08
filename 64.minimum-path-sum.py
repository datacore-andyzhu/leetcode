# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#


# @lc tags=array;dynamic-programming

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
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min((grid[i][j] + dp[i-1][j]),
                            (grid[i][j] + dp[i][j-1]))

        return dp[m-1][n-1]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,3,1],[1,5,1],[4,2,1]]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid = [[1,2,3],[4,5,6]]')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().minPathSum([[1,2,3],[4,5,6]])))
    print()
    
    pass
# @lc main=end

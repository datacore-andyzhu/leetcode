# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)] 
        i = 0
        while i < cols and obstacleGrid[0][i] == 0:
            dp[0][i] = 1
            i += 1
        i = 0
        while i < rows and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows-1][cols-1]


        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('obstacleGrid = [[0,1],[0,0]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().uniquePathsWithObstacles([[0,1],[0,0]])))
    print()
    
    pass
# @lc main=end

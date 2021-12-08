# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#


# @lc tags=hash-table;stack

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
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, n):
            for j in range(n):
                val = matrix[i][j]
                dp[i][j] = dp[i-1][j] + val
                if j - 1 >= 0: 
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+val)
                if j + 1 < n: 
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1]+val)
        
        return min(dp[n-1])
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[2,1,3],[6,5,4],[7,8,9]]')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix = [[-19,57],[-40,-5]]')
    print('Exception :')
    print('-59')
    print('Output :')
    print(str(Solution().minFallingPathSum([[-19,57],[-40,-5]])))
    print()
    
    pass
# @lc main=end

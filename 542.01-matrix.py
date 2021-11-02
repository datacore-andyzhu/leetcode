# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#


# @lc tags=depth-first-search;breadth-first-search

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
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Algorithm

            Iterate over the matrix from top to bottom-left to right:
            Update \text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j-1],\text{dist}[i-1]             [j])+1)dist[i][j]=min(dist[i][j],min(dist[i][j−1],dist[i−1][j])+1) i.e., minimum of the current dist and distance from top or left neighbor +1, that would have been already calculated previously in the current iteration.
            Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
            Update \text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j+1],\text{dist}[i+1][j])+1)dist[i][j]=min(dist[i][j],min(dist[i][j+1],dist[i+1][j])+1) i.e. minimum of current dist and distances calculated from bottom and right neighbors, that would be already available in current iteration.
        """
        if len(mat) == 0:
            return mat
        dp = [[float(inf) for _ in range(len(mat[0]))]
              for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
                else:
                    dp[i][j] = 0
        for k in range(len(mat)-1, -1, -1):
            for l in range(len(mat[0])-1, -1, -1):
                if k < len(mat) - 1:
                    dp[k][l] = min(dp[k][l], dp[k+1][l]+1)
                if l < len(mat[0]) - 1:
                    dp[k][l] = min(dp[k][l], dp[k][l+1]+1)
        return dp
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[0,0,0],[0,1,0],[0,0,0]]')
    print('Exception :')
    print('[[0,0,0],[0,1,0],[0,0,0]]')
    print('Output :')
    print(str(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[0,0,0],[0,1,0],[1,1,1]]')
    print('Exception :')
    print('[[0,0,0],[0,1,0],[1,2,1]]')
    print('Output :')
    print(str(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])))
    print()

    pass
# @lc main=end

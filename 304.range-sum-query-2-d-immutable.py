# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
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


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        # self.matrixSum = [
        #     [0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # for i in range(len(matrix)):
        #     rowsum = 0
        #     for j in range(len(matrix[0])):
        #         rowsum = rowsum + matrix[i][j]
        #         self.matrixSum[i+1][j+1] = self.matrixSum[i][j+1] + rowsum
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return
        self.matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                self.matrix[i+1][j+1] = self.matrix[i+1][j] + self.matrix[i][j+1] + matrix[i][j] - self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrixSum[row2+1][col2+1] - self.matrixSum[row1][col2+1] \
            - self.matrixSum[row2+1][col1] + self.matrixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end

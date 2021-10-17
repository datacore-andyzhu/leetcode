# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc tags=binary-search;divide-and-conquer

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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols-1
        
        while 0 <= row < rows and 0 <= col < cols:
            start = matrix[row][col]
            if target < start:
                col -= 1
            elif target > start:
                row += 1
            else:
                return True
        return False
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target = 20')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20)))
    print()
    
    pass
# @lc main=end

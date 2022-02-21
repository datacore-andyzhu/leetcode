# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#


# @lc tags=hash-table;two-pointers;sliding-window

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
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,1],[1,2]], row = 0, col = 0, color = 3')
    print('Exception :')
    print('[[3,3],[3,2]]')
    print('Output :')
    print(str(Solution().colorBorder([[1,1],[1,2]],0,0,3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3')
    print('Exception :')
    print('[[1,3,3],[2,3,3]]')
    print('Output :')
    print(str(Solution().colorBorder([[1,2,2],[2,3,2]],0,1,3)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2')
    print('Exception :')
    print('[[2,2,2],[2,1,2],[2,2,2]]')
    print('Output :')
    print(str(Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]],1,1,2)))
    print()
    
    pass
# @lc main=end
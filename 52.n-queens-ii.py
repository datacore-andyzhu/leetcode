# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#


# @lc tags=backtracking

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
    def __init__(self) -> None:
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        col, pie, na = set(), set(), set()

        def _dfs(level):
            if level == n:
                self.res += 1
                return
            for j in range(0, n):
                if j in col or level+j in pie or level-j in na:
                    continue
                col.add(j)
                pie.add(level+j)
                na.add(level-j)
                _dfs(level+1)
                col.remove(j)
                pie.remove(level + j)
                na.remove(level-j)

        _dfs(0)
        return self.res
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().totalNQueens(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().totalNQueens(1)))
    print()

    pass
# @lc main=end

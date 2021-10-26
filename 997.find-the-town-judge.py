# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#


# @lc tags=Unknown

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
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # this is the case of count the in-degree and out-degree 
        # of each node in the graph
        # not exactly the case of union find 
        if len(trust) < n - 1:
            return -1
        in_degree = [0] * (n+1)
        out_degree = [0] * (n+1)
        for truster, trustee in trust:
            in_degree[trustee] += 1
            out_degree[truster] += 1
        for i in range(1, n+1):
            if in_degree[i] == n-1 and out_degree[i] == 0:
                return i
        return -1

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2, trust = [[1,2]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findJudge(2, [[1, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, trust = [[1,3],[2,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findJudge(3, [[1, 3], [2, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3, trust = [[1,3],[2,3],[3,1]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 3, trust = [[1,2],[2,3]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findJudge(3, [[1, 2], [2, 3]])))
    print()

    print('Example 5:')
    print('Input : ')
    print('n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findJudge(
        4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])))
    print()

    pass
# @lc main=end

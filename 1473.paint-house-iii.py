# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
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
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
        houses = [c - 1 for c in houses]

        # dp 所有元素初始化为极大值
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue

                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(
                                dp[i][j][k], dp[i - 1][j0][k - 1])

                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float("inf") else ans

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =5, n = 2, target = 3')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().minCost([0, 0, 0, 0, 0], [
          [1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =5, n = 2, target = 3')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().minCost([0, 2, 1, 2, 0], [
          [1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n= 3, target = 3')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minCost([3, 1, 2, 3], [
          [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3)))
    print()

    pass
# @lc main=end

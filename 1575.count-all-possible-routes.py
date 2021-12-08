# @lc app=leetcode id=1575 lang=python3
#
# [1575] Count All Possible Routes
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
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """ Solution 1: top-down approach """
        # n = len(locations)
        # # memo table to store the possible ways at location i with fuel j to reach destionation
        # # memo[i][j], i in {0, len(location)} and j in {0, fuel}
        # memo = [[-1 for _ in range(fuel+1)] for _ in range(n)]
        # mod = 10**9+7

        # def dfs(locations, start, finish, fuel):
        #     if memo[start][fuel] != -1:
        #         return memo[start][fuel]

        #     n = len(locations)

        #     need = abs(locations[start]-locations[finish])
        #     if need > fuel:
        #         memo[start][fuel] == 0
        #         return 0

        #     sum = 0
        #     if start == finish:
        #         sum = 1
        #     for i in range(n):
        #         if i != start:
        #             need = abs(locations[i]-locations[start])
        #             if fuel >= need:
        #                 sum += dfs(locations, i, finish, fuel-need)
        #                 sum %= mod
        #     memo[start][fuel] = sum
        #     return sum

        # return dfs(locations, start, finish, fuel)

        """ Solution 2: botton up approach """
        mod = 10**9+7
        n = len(locations)
        dp = [[0 for _ in range(fuel+1)] for _ in range(n)]
        # for location start point = finish, we only have 1 route
        for i in range(fuel+1):
            dp[finish][i] = 1

        #  // 从状态转移方程可以发现 f[i][fuel]=f[i][fuel]+f[k][fuel-need]
        # // 在计算 f[i][fuel] 的时候依赖于 f[k][fuel-need]
        # // 其中 i 和 k 并无严格的大小关系
        # // 而 fuel 和 fuel-need 具有严格大小关系：fuel >= fuel-need
        # // 因此需要先从小到大枚举油量
        for curr in range(fuel+1):
            for i in range(n):  # start
                for k in range(n):  # finish
                    if k != i:
                        need = abs(locations[i]-locations[k])
                        if curr >= need:
                            dp[i][curr] += dp[k][curr-need]
                            dp[i][curr] %= mod
        return dp[start][fuel]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countRoutes([2, 3, 6, 8, 4], 1, 3, 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('locations = [4,3,1], start = 1, finish = 0, fuel = 6')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().countRoutes([4, 3, 1], 1, 0, 6)))
    print()

    print('Example 3:')
    print('Input : ')
    print('locations = [5,2,1], start = 0, finish = 2, fuel = 3')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countRoutes([5, 2, 1], 0, 2, 3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('locations = [2,1,5], start = 0, finish = 0, fuel = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().countRoutes([2, 1, 5], 0, 0, 3)))
    print()

    print('Example 5:')
    print('Input : ')
    print('locations = [1,2,3], start = 0, finish = 2, fuel = 40')
    print('Exception :')
    print('615088286')
    print('Output :')
    print(str(Solution().countRoutes([1, 2, 3], 0, 2, 40)))
    print()

    pass
# @lc main=end

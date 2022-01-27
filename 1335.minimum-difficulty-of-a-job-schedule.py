# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
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
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """ Solution 1 """
        # https://medium.com/@chuncaohenli/1335-minimum-difficulty-of-a-job-schedule-5ee30d10a88b
        # https://www.youtube.com/watch?v=6EZVJWHt9Qg
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[0] * n] + [[float('inf')] * n for _ in range(d - 1)]
        # dp[0][0] = jobDifficulty[0]
        # for i in range(1, n):
        #     dp[0][i] = max(jobDifficulty[i], dp[0][i - 1])
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, jobDifficulty[i])
            dp[0][i] = max_diff
        for i in range(1, d):
            for j in range(i, n):
                max_r = jobDifficulty[j]
                for r in range(j, i - 1, -1):
                    max_r = max(max_r, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], max_r + dp[i - 1][r - 1])
        return dp[-1][-1]
        """ Solution 2 """
        # n = len(jobDifficulty)
        # if d > n:
        #     return -1

        # # dp[i][k] := min difficulty to schedule the first i jobs in k days
        # dp = [[inf] * (d + 1) for _ in range(n + 1)]
        # dp[0][0] = 0

        # for i in range(1, n + 1):
        #     for k in range(1, d + 1):
        #         maxDifficulty = 0  # max(job[j + 1..i])
        #         for j in range(i - 1, k - 2, -1):  # 1-based
        #             # 0-based
        #             maxDifficulty = max(maxDifficulty, jobDifficulty[j])
        #             dp[i][k] = min(dp[i][k], dp[j][k - 1] + maxDifficulty)

        # return dp[n][d]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('jobDifficulty = [6,5,4,3,2,1], d = 2')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('jobDifficulty = [9,9,9], d = 4')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minDifficulty([9, 9, 9], 4)))
    print()

    print('Example 3:')
    print('Input : ')
    print('jobDifficulty = [1,1,1], d = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minDifficulty([1, 1, 1], 3)))
    print()

    pass
# @lc main=end

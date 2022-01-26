# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#


# @lc tags=stack

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
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp数组，每个元素代表到当前天数最少钱数，为下标方便对应，多加一个 0 位置
        dp = [0 for _ in range(days[-1] + 1)]
        days_idx = 0  # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        for i in range(1, len(dp)):
            if i != days[days_idx]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1

        return dp[-1]  # 返回最后一天对应的费用即可
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('days = [1,4,6,7,8,20], costs = [2,7,15]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])))
    print()

    print('Example 2:')
    print('Input : ')
    print('days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]')
    print('Exception :')
    print('17')
    print('Output :')
    print(str(Solution().mincostTickets(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])))
    print()

    pass
# @lc main=end

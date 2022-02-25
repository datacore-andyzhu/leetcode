# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#


# @lc tags=depth-first-search

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
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        s = sum(matchsticks)
        # 如果周长不能被4整除，直接返回False
        if s % 4 != 0:
            return False
        w = s // 4
        # 先将数组从大到小排序，这里利用了贪心的思路，找到解的速度会快很多
        matchsticks.sort(reverse=True)

        def _dfs(index, w_arr):
            # 数组用完了，边长数组必须都为0，否则返回False
            if index == len(matchsticks):
                return all(i == 0 for i in w_arr)
            for j in range(len(w_arr)):
                # 这里用到了剪枝，如果w_arr连续两个值相同，则可以跳过
                if j > 0 and w_arr[j] == w_arr[j-1]:
                    continue
                # 依次尝试去扣除nums[index]
                if w_arr[j] >= matchsticks[index]:
                    w_arr[j] -= matchsticks[index]
                    if _dfs(index+1, w_arr):
                        return True
                    w_arr[j] += matchsticks[index]
            return False

        return _dfs(0, [w, w, w, w])

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matchsticks = [1,1,2,2,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().makesquare([1, 1, 2, 2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matchsticks = [3,3,3,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().makesquare([3, 3, 3, 3, 4])))
    print()

    pass
# @lc main=end

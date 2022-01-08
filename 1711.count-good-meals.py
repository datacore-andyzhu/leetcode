# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
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
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = pow(10, 9)+7
        max_pow_2 = 1 << 22
        map = {}

        ans = 0
        for num in deliciousness:
            i = 1
            while i < max_pow_2:
                t = i - num
                if t in map:
                    ans += map[t]
                    if ans >= mod:
                        ans -= mod
                i = i << 1
            if map.get(num, 0) == 0:
                map[num] = 1
            else:
                map[num] += 1

        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('deliciousness = [1,3,5,7,9]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countPairs([1, 3, 5, 7, 9])))
    print()

    print('Example 2:')
    print('Input : ')
    print('deliciousness = [1,1,1,3,3,3,7]')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().countPairs([1, 1, 1, 3, 3, 3, 7])))
    print()

    pass
# @lc main=end

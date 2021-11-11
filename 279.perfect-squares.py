# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#


# @lc tags=math;dynamic-programming;breadth-first-search

# @lc imports=start
import collections
import math
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
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(int(math.sqrt(n)+1))]
        ans = 1
        queue = collections.deque([n])

        while queue:
            size = len(queue)
            for _ in range(size):
                num = queue.popleft()
                for s in squares:
                    if s == num:
                        return ans
                    if s > num:
                        break
                    queue.append(num-s)
            ans += 1
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 12')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numSquares(12)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 13')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numSquares(13)))
    print()

    pass
# @lc main=end

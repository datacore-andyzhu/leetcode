# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#


# @lc tags=greedy

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
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i = j = count = 0
        while i < m and j < n:
            while j < n and g[i] > s[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1
        return count
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('g = [1,2,3], s = [1,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findContentChildren([1, 2, 3], [1, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('g = [1,2], s = [1,2,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findContentChildren([1, 2], [1, 2, 3])))
    print()

    pass
# @lc main=end

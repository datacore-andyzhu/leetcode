# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#


# @lc tags=binary-search

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
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        def binarySearchBoundary(low, high):
            while low < high:
                mid = low + (high-low) // 2
                if isBadVersion(mid) == True:
                    high = mid
                elif isBadVersion(mid) == False:
                    low = mid + 1
            if low >= n or isBadVersion(low) != True:
                return -1
            return low
        return binarySearchBoundary(0, n)
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, bad = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().firstBadVersion(5, bad=4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, bad = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().firstBadVersion(1, bad=1)))
    print()

    pass
# @lc main=end

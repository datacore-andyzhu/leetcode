# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#


# @lc tags=array;hash-table;binary-search;dynamic-programming

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
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_count = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_count = max(max_count, dp[i][j])

        return max_count
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])))
    print()

    pass
# @lc main=end

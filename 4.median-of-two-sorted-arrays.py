# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc tags=array;binary-search;divide-and-conquer

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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        total_left = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            left_i = -math.inf if i == 0 else nums1[i - 1]
            left_j = -math.inf if j == 0 else nums2[j - 1]

            right_i = math.inf if i == m else nums1[i]
            right_j = math.inf if j == n else nums2[j]

            if left_i <= right_j:
                median1 = max(left_i, left_j)
                median2 = min(right_i, right_j)
                left = i + 1
            else:
                right = i - 1

        if (m + n) % 2 == 0:
            return (median1 + median2) / 2
        else:
            return median1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,3], nums2 = [2]')
    print('Exception :')
    print('2.00000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,3],[2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [3,4]')
    print('Exception :')
    print('2.50000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,2],[3,4])))
    print()
    
    pass
# @lc main=end

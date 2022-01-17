# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#


# @lc tags=array

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
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ Solution 1:  trinary """
#         left = 0
#         right = len(arr) - 1
#         while left < right:
#             m1 = left + (right - left) // 3
#             m2 = right - (right - left) // 3
#             if arr[m1] > arr[m2]:
#                 right = m2 -1
#             else:
#                 left = m1 + 1

#         return right

        """ Solution 2: binary search """
#         left = 1
#         right = len(arr) - 1
#         while left < right:
#             mid = left + right + 1 >> 1
#             if arr[mid-1] < arr[mid]:
#                 left = mid
#             else:
#                 right = mid - 1

#         return right

        """ Solution 3 """
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
    pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [0,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 1, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [0,2,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 2, 1, 0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [0,10,5,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().peakIndexInMountainArray([0, 10, 5, 2])))
    print()

    pass
# @lc main=end

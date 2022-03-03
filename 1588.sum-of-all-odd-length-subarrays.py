# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
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
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
        sumx = 0
        for i in range(n):
            length = 1
            while i + length <= n:
                end = i + length - 1
                sumx += prefix_sum[end+1] - prefix_sum[i]
                length += 2
        return sumx
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,4,2,5,3]')
    print('Exception :')
    print('58')
    print('Output :')
    print(str(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().sumOddLengthSubarrays([1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [10,11,12]')
    print('Exception :')
    print('66')
    print('Output :')
    print(str(Solution().sumOddLengthSubarrays([10, 11, 12])))
    print()

    pass
# @lc main=end

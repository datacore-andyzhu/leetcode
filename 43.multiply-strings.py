# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#


# @lc tags=math;string

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
    def multiply(self, num1: str, num2: str) -> str:
        # Make num2 smaller than nums1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        sum = 0
        for digit2 in num2:
            _subsum = 0
            for idx, digit1 in enumerate(num1[::-1]):
                _subsum = _subsum + (int(digit2) * int(digit1)) * (10 ** (idx))
            sum = sum * 10 + _subsum
        return str(sum)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "2", num2 = "3"')
    print('Exception :')
    print('"6"')
    print('Output :')
    print(str(Solution().multiply("2", "3")))
    print()

    print('Example 2:')
    print('Input : ')
    print('num1 = "123", num2 = "456"')
    print('Exception :')
    print('"56088"')
    print('Output :')
    print(str(Solution().multiply("123", "456")))
    print()

    pass
# @lc main=end

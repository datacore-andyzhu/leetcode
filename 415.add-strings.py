# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc tags=string

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
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = []
        # make sure num1 is shorter
        if len(num1) > len(num2):
            num1, num2 = num2, num1
            # fill up 0 to num1 to have the same length as num2
        if len(num2) - len(num1) > 0:
            add_zero = '0' * (len(num2) - len(num1))
            num1 = add_zero + num1
        for i in range(len(num1)-1, -1, -1):
            temp = int(num1[i]) + int(num2[i]) + carry
            if temp >= 10:
                carry = 1
            else:
                carry = 0
            temp = temp % 10
            result.append(str(temp))
        if carry == 1:
            result.append(str(carry))
        result = result[::-1]
        result = ''.join(result)
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "11", num2 = "123"')
    print('Exception :')
    print('"134"')
    print('Output :')
    print(str(Solution().addStrings("11", "123")))
    print()

    print('Example 2:')
    print('Input : ')
    print('num1 = "456", num2 = "77"')
    print('Exception :')
    print('"533"')
    print('Output :')
    print(str(Solution().addStrings("456", "77")))
    print()

    print('Example 3:')
    print('Input : ')
    print('num1 = "0", num2 = "0"')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().addStrings("0", "0")))
    print()

    pass
# @lc main=end

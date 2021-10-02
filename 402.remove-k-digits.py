# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#


# @lc tags=stack;greedy

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
    def removeKdigits(self, num: str, k: int) -> str:
        # use monotone stack to solve this issue
        # use ever increase monotone stack
        # edge case
        if len(num) <= k:
            return "0"

        montone_stack = []
        for i in range(len(num)):
            while k > 0 and montone_stack and montone_stack[-1] > num[i]:
                montone_stack.pop()
                k -= 1
            if not (num[i] == '0' and len(montone_stack) == 0):
                montone_stack.append(num[i])

        # if we ever encountered an already sorted array of numbers
        # like num = "123456789" and k = 3
        # we also need to consider the situation 
        # where k larger than the lenth of the stack
        # num = "10001" and k = 4
        while k > 0 and len(montone_stack) > 0:
            montone_stack.pop()
            k -= 1
        if len(montone_stack) == 0:
            return "0"
        else:
            return "".join(montone_stack)
    
    # def removeKdigits(self, num, k):
    #     stack = []
    #     remain = len(num) - k
    #     for digit in num:
    #         while k and stack and stack[-1] > digit:
    #             stack.pop()
    #             k -= 1
    #         stack.append(digit)
            # we do not need to necessary remove the remove k letters 
            # at the end of the string we just need to taking first len(num)-k slots
            # but this will present a problem is what if the rest of stack does not have
            # that length
    #     return ''.join(stack[:remain]).lstrip('0') or '0'


# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = "1432219", k = 3')
    print('Exception :')
    print('"1219"')
    print('Output :')
    print(str(Solution().removeKdigits("1432219", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = "10200", k = 1')
    print('Exception :')
    print('"200"')
    print('Output :')
    print(str(Solution().removeKdigits("10200", 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = "10", k = 2')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().removeKdigits("10", 2)))
    print()

    pass
# @lc main=end

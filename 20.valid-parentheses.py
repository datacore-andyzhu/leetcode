# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc tags=string;stack

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
    def isPair(self, stack, input):
        return stack == '(' and input == ')' or \
            stack == '[' and input == ']' or \
            stack == '{' and input == '}'

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if stack != [] and self.isPair(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
                    
        return not stack

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("()")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "()[]{}"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("()[]{}")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "(]"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("(]")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "([)]"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("([)]")))
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "{[]}"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("{[]}")))
    print()

    pass
# @lc main=end

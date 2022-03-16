# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
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
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack = []

        # # for i in range(len(s)): # we do not use range(lens(s)) here because
        # # the s has changed when we remove the (, but len(s) inside the
        # # range function only compute the len of s once, while
        # # we need to recompute the len of s every loop
        # i = 0
        # while i < len(s):
        #     if not stack and s[i] == ')':
        #         s = s[:i] + s[i+1:]
        #         continue
        #     if s[i] == '(':
        #         stack.append(['(', i])

        #     if s[i] == ')':
        #         if stack[-1][0] == '(':
        #             stack.pop()
        #     i += 1
        # while stack:
        #     idx = stack[-1][1]
        #     s = s[:idx] + s[idx+1:]
        #     stack.pop()
        # return s
        """ Solution 2 """
        first_pass = []
        balance = 0
        open_seen = 0
        for ch in s:
            if ch == "(":
                open_seen += 1
                balance += 1
            if ch == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass.append(ch)
        result = []
        open_keep = open_seen - balance
        for ch in first_pass:
            if ch == "(":
                open_keep -= 1
                if open_keep < 0:
                    continue
            result.append(ch)
        return ''.join(result)
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "lee(t(c)o)de)"')
    print('Exception :')
    print('"lee(t(c)o)de"')
    print('Output :')
    print(str(Solution().minRemoveToMakeValid("lee(t(c)o)de)")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a)b(c)d"')
    print('Exception :')
    print('"ab(c)d"')
    print('Output :')
    print(str(Solution().minRemoveToMakeValid("a)b(c)d")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "))(("')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().minRemoveToMakeValid("))((")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "(a(b(c)d)"')
    print('Exception :')
    print('"a(b(c)d)"')
    print('Output :')
    print(str(Solution().minRemoveToMakeValid("(a(b(c)d)")))
    print()

    pass
# @lc main=end

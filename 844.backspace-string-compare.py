# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
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
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ Solution 1: Use stack """
        # stack1 = []
        # for char in s:
        #     if char == '#' and len(stack1) == 0:
        #         continue
        #     elif char == '#' and len(stack1) != 0:
        #         stack1.pop()
        #     else:
        #         stack1.append(char)
        # stack2 = []
        # for char in t:
        #     if char == '#' and len(stack2) == 0:
        #         continue
        #     elif char == '#' and len(stack2) != 0:
        #         stack2.pop()
        #     else:
        #         stack2.append(char)

        # return stack1 == stack2

        """ Solution 2: two pointers"""
        import itertools

        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ab#c", t = "ad#c"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().backspaceCompare("ab#c", "ad#c")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ab##", t = "c#d#"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().backspaceCompare("ab##", "c#d#")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a##c", t = "#a#c"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().backspaceCompare("a##c", "#a#c")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "a#c", t = "b"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().backspaceCompare("a#c", "b")))
    print()

    pass
# @lc main=end

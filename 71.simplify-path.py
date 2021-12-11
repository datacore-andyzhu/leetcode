# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
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
    def simplifyPath(self, path: str) -> str:
        result = '/'
        stack = []
        temp_list = path.split('/')
        for item in temp_list:
            if item == '..' and len(stack) == 0:
                continue
            elif item == '..' and len(stack) != 0:
                stack.pop()
            elif item == '.':
                continue
            else:
                if len(item) != 0:
                    stack.append(item)
        # print(stack)
        result += '/'.join(stack)
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('path = "/home/"')
    print('Exception :')
    print('"/home"')
    print('Output :')
    print(str(Solution().simplifyPath("/home/")))
    print()

    print('Example 2:')
    print('Input : ')
    print('path = "/../"')
    print('Exception :')
    print('"/"')
    print('Output :')
    print(str(Solution().simplifyPath("/../")))
    print()

    print('Example 3:')
    print('Input : ')
    print('path = "/home//foo/"')
    print('Exception :')
    print('"/home/foo"')
    print('Output :')
    print(str(Solution().simplifyPath("/home//foo/")))
    print()

    print('Example 4:')
    print('Input : ')
    print('path = "/a/./b/../../c/"')
    print('Exception :')
    print('"/c"')
    print('Output :')
    print(str(Solution().simplifyPath("/a/./b/../../c/")))
    print()

    pass
# @lc main=end

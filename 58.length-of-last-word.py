# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
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
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        real_string = [word for word in temp if len(temp) != 0]
        return len(real_string[-1])

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Hello World"')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().lengthOfLastWord("Hello World")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "   fly me   to   the moon  "')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLastWord("   fly me   to   the moon  ")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "luffy is still joyboy"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().lengthOfLastWord("luffy is still joyboy")))
    print()

    pass
# @lc main=end

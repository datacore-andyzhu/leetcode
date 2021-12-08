# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc tags=two-pointers;string

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
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        str_list = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            if str_list[start] in vowels and str_list[end] in vowels:
                str_list[start], str_list[end] = str_list[end], str_list[start]
                start += 1
                end -= 1
            elif str_list[start] not in vowels:
                start += 1
            elif str_list[end] not in vowels:
                end -= 1
        return ''.join(str_list)

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "hello"')
    print('Exception :')
    print('"holle"')
    print('Output :')
    print(str(Solution().reverseVowels("hello")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "leetcode"')
    print('Exception :')
    print('"leotcede"')
    print('Output :')
    print(str(Solution().reverseVowels("leetcode")))
    print()

    pass
# @lc main=end

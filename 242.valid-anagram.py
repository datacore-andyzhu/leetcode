# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc tags=hash-table;sort

# @lc imports=start
import collections
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
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # source = [0] * 26
        # for char in s:
        #     source[ord(char)-ord('a')] += 1
        # for char in t:
        #     source[ord(char)-ord('a')] -= 1
        # for num in source:
        #     if num != 0:
        #         return False
        # return True
        return collections.Counter(s) == collections.Counter(t)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "anagram", t = "nagaram"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isAnagram("anagram", "nagaram")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "rat", t = "car"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isAnagram("rat", "car")))
    print()

    pass
# @lc main=end

# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
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
    def longestCommonPrefix(self, strs: List[str]) -> str:

        base = strs[0]

        result = ''
        for i in range(len(base)):
            for word in strs[1:]:
                if i >= len(word):
                    return result # return result, not the base string
                if base[i] != word[i]:
                    return result
            result += base[i]
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["flower","flow","flight"]')
    print('Exception :')
    print('"fl"')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["flower", "flow", "flight"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["dog","racecar","car"]')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["dog", "racecar", "car"])))
    print()

    pass
# @lc main=end

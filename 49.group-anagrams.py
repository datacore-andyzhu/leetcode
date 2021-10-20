# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc tags=hash-table;string

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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        str_sum_dict = {}
        for _str in strs:
            key = ''.join(sorted(_str))
            if key in str_sum_dict:
                str_sum_dict[key].append(_str)
            else:
                str_sum_dict[key] = [_str]
        return list(str_sum_dict.values())

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["eat","tea","tan","ate","nat","bat"]')
    print('Exception :')
    print('[["bat"],["nat","tan"],["ate","eat","tea"]]')
    print('Output :')
    print(str(Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = [""]')
    print('Exception :')
    print('[[""]]')
    print('Output :')
    print(str(Solution().groupAnagrams([""])))
    print()

    print('Example 3:')
    print('Input : ')
    print('strs = ["a"]')
    print('Exception :')
    print('[["a"]]')
    print('Output :')
    print(str(Solution().groupAnagrams(["a"])))
    print()

    pass
# @lc main=end

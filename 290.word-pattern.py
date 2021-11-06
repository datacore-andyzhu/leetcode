# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc tags=hash-table

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
import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # bijection: each element in set A has one-to-one mapping to another element of set B
        """ 
        the following code is wrong, because it failed the following scenario:
        pattern='abba' 
        s = 'dog dog dog dog'
        That's why you need two way mapping        
        """
        # string_list = s.split(' ')
        # if len(set(pattern)) != len(set(string_list)):
        #     return False
        # if len(pattern) != len(string_list):
        #     return False
        # pattern_dict = collections.defaultdict(List)
        # for i in range(len(pattern)):
        #     if pattern[i] not in pattern_dict:
        #         pattern_dict[pattern[i]] = string_list[i]
        #     else:
        #         if pattern_dict[pattern[i]] != string_list[i]:
        #             return False
        # return True
        """ Method 2 """
        # bijection: each element in set A has one-to-one mapping to another element of set B
        s = s.split()
        if len(s) != len(pattern):
            return False
        PtoS = {}
        StoP = {}
        for i in range(len(pattern)):
            cur_letter = pattern[i]
            cur_word = s[i]
            if cur_letter not in PtoS and cur_word not in StoP:
                PtoS[cur_letter] = cur_word
                StoP[cur_word] = cur_letter
            elif PtoS.get(cur_letter) != cur_word or StoP.get(cur_word) != cur_letter:
                return False
        return True
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('pattern = "abba", s = "dog cat cat dog"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog cat cat dog")))
    print()

    print('Example 2:')
    print('Input : ')
    print('pattern = "abba", s = "dog cat cat fish"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog cat cat fish")))
    print()

    print('Example 3:')
    print('Input : ')
    print('pattern = "aaaa", s = "dog cat cat dog"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("aaaa", "dog cat cat dog")))
    print()

    print('Example 4:')
    print('Input : ')
    print('pattern = "abba", s = "dog dog dog dog"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog dog dog dog")))
    print()

    pass
# @lc main=end

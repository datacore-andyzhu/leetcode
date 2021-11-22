# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#


# @lc tags=hash-table

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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_p = collections.Counter(p)
        len_of_p = len(p)
        dict_s = {}
        left = 0
        right = 0

        result = []
        while right < len(s):
            letter = s[right]
            dict_s[letter] = dict_s.get(letter, 0) + 1

            while right - left + 1 >= len_of_p:
                if dict_s == dict_p:
                    result.append(left)
                _letter = s[left]
                dict_s[_letter] -= 1
                if dict_s[_letter] == 0:
                    del dict_s[_letter]

                left += 1
            right += 1
        return result

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "cbaebabacd", p = "abc"')
    print('Exception :')
    print('[0,6]')
    print('Output :')
    print(str(Solution().findAnagrams("cbaebabacd","abc")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "abab", p = "ab"')
    print('Exception :')
    print('[0,1,2]')
    print('Output :')
    print(str(Solution().findAnagrams("abab","ab")))
    print()
    
    pass
# @lc main=end

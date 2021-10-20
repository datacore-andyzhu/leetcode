# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
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
    def longestPalindrome(self, s: str) -> int:
        char_counter = collections.Counter(s)
        count = 0
        for key, value in char_counter.items():
            count += value // 2
        count *= 2

        return min(len(s), count+1)
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abccccdd"')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().longestPalindrome("abccccdd")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().longestPalindrome("a")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "bb"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().longestPalindrome("bb")))
    print()
    
    pass
# @lc main=end
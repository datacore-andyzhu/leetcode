# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
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
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('haystack = "hello", needle = "ll"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().strStr("hello","ll")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('haystack = "aaaaa", needle = "bba"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().strStr("aaaaa","bba")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('haystack = "", needle = ""')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().strStr("","")))
    print()
    
    pass
# @lc main=end
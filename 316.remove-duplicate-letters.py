# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#


# @lc tags=stack;greedy

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
    def removeDuplicateLetters(self, s: str) -> str:
        letter_counter = collections.Counter(s)
        monotone_stack = []
        for char in s:
            if char not in monotone_stack:
                while monotone_stack and monotone_stack[-1] > char and letter_counter[monotone_stack[-1]] > 0:
                    monotone_stack.pop()
                monotone_stack.append(char)
            letter_counter[char] -= 1
        
        return ''.join(monotone_stack)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "bcabc"')
    print('Exception :')
    print('"abc"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("bcabc")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "cbacdcbc"')
    print('Exception :')
    print('"acdb"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("cbacdcbc")))
    print()
    
    pass
# @lc main=end

# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc tags=hash-table;two-pointers;string;sliding-window

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
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_window = collections.defaultdict(int)
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            c = s[right]
            right += 1 
            sliding_window[c] += 1

            while sliding_window[c] > 1:
                d = s[left]
                left += 1
                sliding_window[d] -= 1
            max_len = max(max_len, right-left)

        return max_len
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abcabcbb"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("abcabcbb")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "bbbbb"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("bbbbb")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "pwwkew"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("pwwkew")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = ""')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("")))
    print()
    
    pass
# @lc main=end
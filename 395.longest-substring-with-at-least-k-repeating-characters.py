# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#


# @lc tags=Unknown

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
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        left = 0
        right = 0
        windows = [0]*26
        substr_length = 0
        while right < len(s):
            char = s[right]
            windows[ord(char) - ord('a')] += 1
            right += 1
            while min(windows) >= k:
                char = s[left]
                windows[ord(char) - ord('a')] -= 1
                substr_length = max(substr_length, right-left+1)
                left -= 1
        return substr_length
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aaabb", k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().longestSubstring("aaabb", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ababbc", k = 2')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().longestSubstring("ababbc", 2)))
    print()

    pass
# @lc main=end

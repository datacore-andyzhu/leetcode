# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc tags=two-pointers;sliding-window

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
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        ans = left = right = 0
        while right < n:
            num[ord(s[right]) - ord('A')] += 1
            maxn = max(num)
            while right - left + 1 - maxn > k:
                num[ord(s[left]) - ord('A')] -= 1
                maxn = max(num)
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ABAB", k = 2')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("ABAB", 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "AABABBA", k = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("AABABBA", 1)))
    print()

    pass
# @lc main=end

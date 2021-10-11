# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
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
    def minWindow(self, s: str, t: str) -> str:
        """
        Use sliding window techniq to solve this issue
        """
        pattern_dict = collections.Counter(t)
        slidng_window = collections.defaultdict(int)
        left = 0
        right = 0
        valid = 0
        min_len = float('inf')
        # store the index where the minimum subsctring start
        start = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in pattern_dict:
                slidng_window[c] += 1
                if slidng_window[c] == pattern_dict[c]:
                    valid += 1

            while valid == len(pattern_dict):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                d = s[left]
                left += 1
                if d in pattern_dict:
                    if slidng_window[d] == pattern_dict[d]:
                        valid -= 1
                    slidng_window[d] -= 1

        return "" if min_len == float('inf') else s[start:(start+min_len)]

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ADOBECODEBANC", t = "ABC"')
    print('Exception :')
    print('"BANC"')
    print('Output :')
    print(str(Solution().minWindow("ADOBECODEBANC", "ABC")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a", t = "a"')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().minWindow("a", "a")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a", t = "aa"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().minWindow("a", "aa")))
    print()

    pass
# @lc main=end

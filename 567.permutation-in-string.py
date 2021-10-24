# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def convertStrtoDict(s):
            dict = defaultdict(int)
            for char in s:
                dict[char] += 1
            return dict
        # missing the special case:
        if len(s1) > len(s2):
            return False
        base_dict = defaultdict(int)
        for char in s1:
            base_dict[char] += 1
        left = 0
        right = len(s1)
        while right <= len(s2):
            if convertStrtoDict(s2[left:right]) == base_dict:
                return True
            right += 1
            left += 1
        return False

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "ab", s2 = "eidbaooo"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkInclusion("ab", "eidbaooo")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "ab", s2 = "eidboaoo"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkInclusion("ab", "eidboaoo")))
    print()

    pass
# @lc main=end

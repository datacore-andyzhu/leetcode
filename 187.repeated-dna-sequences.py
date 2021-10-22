# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#


# @lc tags=hash-table;bit-manipulation

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
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        left = 0
        right = left + 10
        counter = collections.defaultdict()
        while right <= len(s):
            if s[left:right] not in counter:
                counter[s[left:right]] = 1
            else:
                counter[s[left:right]] += 1
            left += 1
            right = left + 10
        result = []
        for key, value in counter.items():
            if value > 1:
                result.append(key)

        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"')
    print('Exception :')
    print('["AAAAACCCCC","CCCCCAAAAA"]')
    print('Output :')
    print(str(Solution().findRepeatedDnaSequences(
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "AAAAAAAAAAAAA"')
    print('Exception :')
    print('["AAAAAAAAAA"]')
    print('Output :')
    print(str(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")))
    print()

    pass
# @lc main=end

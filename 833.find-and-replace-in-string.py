# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#


# @lc tags=breadth-first-search

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
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ''
        combo = {}
        for i in range(len(indices)):
            combo[indices[i]] = [sources[i], targets[i]]

        # sort the indices
        indices.sort()
        # re-arrange the src and dst according to the new sorted indices
        src = []
        dst = []
        for i in range(len(indices)):
            src.append(combo[indices[i]][0])
            dst.append(combo[indices[i]][1])
        start = 0
        for idx, i in enumerate(indices):
            if s[i:i+len(src[idx])] == src[idx]:
                ans += s[start:i] + dst[idx]
                start = i + len(src[idx])
            else:
                if idx < len(indices) - 1:
                    ans += s[start:indices[idx+1]]
                    start = indices[idx+1]
        ans += s[start:]
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        's = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee","ffff"]')
    print('Exception :')
    print('"eeebffff"')
    print('Output :')
    print(str(Solution().findReplaceString(
        "abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "abcd", indices = [0, 2], sources = ["ab","ec"], targets =["eee","ffff"]')
    print('Exception :')
    print('"eeecd"')
    print('Output :')
    print(str(Solution().findReplaceString(
        "abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])))
    print()

    pass
# @lc main=end

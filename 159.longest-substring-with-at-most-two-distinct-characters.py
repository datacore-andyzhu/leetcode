from collections import *
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        mydict = defaultdict(int)
        ans = -1
        while right < n:
            ch_r = s[right]
            mydict[ch_r] += 1

            while len(mydict) > 2:
                ch_l = s[left]
                mydict[ch_l] -= 1
                if mydict[ch_l] == 0:
                    del mydict[ch_l]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans

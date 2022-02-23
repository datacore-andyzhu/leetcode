import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dict1 = collections.defaultdict(int)
        ans = 0
        while right < len(s):
            dict1[s[right]] += 1
            while len(dict1) > k:
                dict1[s[left]] -= 1
                if dict1[s[left]] == 0:
                    del dict1[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans

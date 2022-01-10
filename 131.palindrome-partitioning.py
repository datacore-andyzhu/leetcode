# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc tags=backtracking

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
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, start, end):
            i = start
            j = end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        results = []

        def backtrack(s, idx, path):
            if idx >= len(s):
                results.append(path[:])
                return
            for i in range(idx, len(s)):
                if isPalindrome(s, idx, i):
                    path.append(s[idx:i+1])
                    backtrack(s, i+1, path)
                    path.pop()
                else:
                    continue

        backtrack(s, 0, [])

        return results
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aab"')
    print('Exception :')
    print('[["a","a","b"],["aa","b"]]')
    print('Output :')
    print(str(Solution().partition("aab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('[["a"]]')
    print('Output :')
    print(str(Solution().partition("a")))
    print()

    pass
# @lc main=end

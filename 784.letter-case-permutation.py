# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#


# @lc tags=tree

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
    def letterCasePermutation(self, s: str) -> List[str]:
        """ Solution 1: recursive """
        # sol = []
        # sl = list(s)
        # def perm(start):
        #     if start == len(sl):
        #         sol.append("".join(sl))
        #         return
        #     perm(start+1)
        #     if sl[start].isalpha():
        #         sl[start] = sl[start].swapcase()
        #         perm(start+1)
        #         sl[start] = sl[start].swapcase()
        # perm(0)
        # return sol

        """ Solution 2: backtracking """
        def backtrack(s, idx, path):
            if idx >= len(s):
                result.append(path[:])
                return

            ch = s[idx]
            if ch.isalpha():
                lower = path + ch.lower()
                upper = path + ch.upper()
                backtrack(s, idx+1, path+ch.lower())
                backtrack(s, idx+1, path+ch.upper())
            else:
                backtrack(s, idx+1, path+ch)

        result = []
        backtrack(s, 0, '')
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "a1b2"')
    print('Exception :')
    print('["a1b2","a1B2","A1b2","A1B2"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("a1b2")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "3z4"')
    print('Exception :')
    print('["3z4","3Z4"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("3z4")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "12345"')
    print('Exception :')
    print('["12345"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("12345")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "0"')
    print('Exception :')
    print('["0"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("0")))
    print()

    pass
# @lc main=end

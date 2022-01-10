# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#


# @lc tags=string;backtracking

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
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s, start, end):
            if start > end:
                return False
            if s[start] == '0' and start != end:
                return False
            if not (0 <= int(s[start:end+1]) <= 255):
                return False
            return True

        results = []

        def backtrack(s, idx, numPeriods):
            # base case
            if numPeriods == 3:
                if isValid(s, idx, len(s)-1):
                    results.append(s[:])
                return
            # level recursion
            for i in range(idx, len(s)):
                if isValid(s, idx, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    backtrack(s, i+2, numPeriods+1)
                    s = s[:i+1] + s[i+2:]
                else:
                    break

        if len(s) > 12:
            return results
        backtrack(s, 0, 0)
        return results

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "25525511135"')
    print('Exception :')
    print('["255.255.11.135","255.255.111.35"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("25525511135")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "0000"')
    print('Exception :')
    print('["0.0.0.0"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("0000")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "101023"')
    print('Exception :')
    print('["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("101023")))
    print()

    pass
# @lc main=end

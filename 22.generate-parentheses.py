# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
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
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(remaining_left, remaining_right, path):
            # at any point creating the pairs, left parenthes should be more than right
            if remaining_left > remaining_right:
                return
            if remaining_left < 0 or remaining_right < 0:
                return
            if remaining_left == 0 and remaining_right == 0:
                result.append(''.join(path.copy()))
                return
            path.append('(')
            backtrack(remaining_left-1, remaining_right, path)
            path.pop()
            path.append(')')
            backtrack(remaining_left, remaining_right-1, path)
            path.pop()
        result = []
        backtrack(n, n, [])
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('["((()))","(()())","(())()","()(())","()()()"]')
    print('Output :')
    print(str(Solution().generateParenthesis(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('["()"]')
    print('Output :')
    print(str(Solution().generateParenthesis(1)))
    print()

    pass
# @lc main=end

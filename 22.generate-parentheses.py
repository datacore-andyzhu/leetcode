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
        """ Solution 1: backtrack """
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

        """" Solution 2: recursion """
        def _dfs(left, right, path):
            # 1. 判断终止条件
            if left == right == 0:
                res.append(path)
                return
            # 2. 处理当前逻辑
            # 3. 不断下探
            if left > 0:
                _dfs(left-1, right, path + '(')
            if right > left:
                _dfs(left, right-1, path + ')')
        res = []
        _dfs(n, n, '')
        return res

        """ Solution 3: BFS """
        res, queue = [], []
        queue.append(('', n, n))
        while queue:
            path, left, right = queue.pop(0)
            if left == right == 0:
                res.append(path)
                continue
            if left > 0:
                queue.append((path+'(', left-1, right))
            if right > left:
                queue.append((path+')', left, right-1))
        return res

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

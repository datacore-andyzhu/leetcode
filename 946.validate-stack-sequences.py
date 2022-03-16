# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#


# @lc tags=math;greedy

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
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('pushed = [1,2,3,4,5], popped = [4,5,3,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validateStackSequences(
        [1, 2, 3, 4, 5], [4, 5, 3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('pushed = [1,2,3,4,5], popped = [4,3,5,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validateStackSequences(
        [1, 2, 3, 4, 5], [4, 3, 5, 1, 2])))
    print()

    pass
# @lc main=end

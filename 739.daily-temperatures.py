# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc tags=hash-table;stack

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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    answer[idx] = i - idx
                stack.append(i)
        return answer
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('temperatures = [73,74,75,71,69,72,76,73]')
    print('Exception :')
    print('[1,1,4,2,1,1,0,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([73,74,75,71,69,72,76,73])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('temperatures = [30,40,50,60]')
    print('Exception :')
    print('[1,1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30,40,50,60])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('temperatures = [30,60,90]')
    print('Exception :')
    print('[1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30,60,90])))
    print()
    
    pass
# @lc main=end
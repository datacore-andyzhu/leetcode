# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#


# @lc tags=stack

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
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:
                stack.append(new)
        return stack
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('asteroids = [5,10,-5]')
    print('Exception :')
    print('[5,10]')
    print('Output :')
    print(str(Solution().asteroidCollision([5,10,-5])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('asteroids = [8,-8]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().asteroidCollision([8,-8])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('asteroids = [10,2,-5]')
    print('Exception :')
    print('[10]')
    print('Output :')
    print(str(Solution().asteroidCollision([10,2,-5])))
    print()
    
    pass
# @lc main=end
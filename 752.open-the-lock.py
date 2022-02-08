# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#


# @lc tags=bit-manipulation

# @lc imports=start
import collections
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
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        if target in deadends:
            return -1
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0

        queue = collections.deque(['0000'])
        visited.add('0000')
        steps = 0
        while queue:
            size = len(queue)
            steps += 1
            for _ in range(size):
                lock = queue.popleft()
                for wheel in range(4):
                    for turn_dir in [-1, 1]:
                        wheel_num = int(lock[wheel])
                        if wheel_num == 0 and turn_dir == -1:
                            new_wheel_num = 9
                        elif wheel_num == 9 and turn_dir == 1:
                            new_wheel_num = 0
                        else:
                            new_wheel_num = wheel_num + turn_dir

                        new_lock = lock[:wheel] + \
                            str(new_wheel_num) + lock[wheel+1:]
                        if new_lock in deadends:
                            # return -1
                            continue
                        if new_lock == target:
                            return steps
                        if new_lock not in visited:
                            queue.append(new_lock)
                            visited.add(new_lock)
        return -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('deadends = ["0201","0101","0102","1212","2002"], target = "0202"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().openLock(["0201","0101","0102","1212","2002"],"0202")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('deadends = ["8888"], target = "0009"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().openLock(["8888"],"0009")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],target = "8888"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('deadends = ["0000"], target = "8888"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().openLock(["0000"],"8888")))
    print()
    
    pass
# @lc main=end

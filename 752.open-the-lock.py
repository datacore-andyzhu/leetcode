# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#


# @lc tags=bit-manipulation

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
    def openLock(self, deadends: List[str], target: str) -> int:
        
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
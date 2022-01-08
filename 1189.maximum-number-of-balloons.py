# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#


# @lc tags=Unknown

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
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        lookup = list('balloon')
        for c in text:
            if c in lookup:
                balloon[c] += 1
        for key, value in balloon.items():
            if key in ['l', 'o']:
                balloon[key] = balloon[key] // 2
            if value == 0:
                return 0
        return min(balloon.values())
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('text = "nlaebolko"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxNumberOfBalloons("nlaebolko")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('text = "loonbalxballpoon"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxNumberOfBalloons("loonbalxballpoon")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('text = "leetcode"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxNumberOfBalloons("leetcode")))
    print()
    
    pass
# @lc main=end

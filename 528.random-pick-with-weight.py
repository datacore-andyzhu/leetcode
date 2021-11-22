# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
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

    def __init__(self, w: List[int]):
        self.total_wright = sum(w)
        self.weights = []
        for idx, value in enumerate(w):
            ratio = ceil(value/self.total_wright*100)
            
            self.weights += [idx] * ratio

    def pickIndex(self) -> int:
        return random.choice(self.weights)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()
    
    pass
# @lc main=end
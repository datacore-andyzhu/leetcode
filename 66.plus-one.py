# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc tags=array

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
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0
        
        for idx, digit in enumerate(digits[::-1]):
            if idx == 0:
                _sum = (digit + carry + 1) % 10
                carry = (digit + carry + 1) // 10
            else:
                _sum = (digit + carry) % 10
                carry = (digit + carry) // 10
            result.append(_sum)
        if carry > 0:
            result.append(carry)
        return result[::-1]
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('digits = [1,2,3]')
    print('Exception :')
    print('[1,2,4]')
    print('Output :')
    print(str(Solution().plusOne([1,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('digits = [4,3,2,1]')
    print('Exception :')
    print('[4,3,2,2]')
    print('Output :')
    print(str(Solution().plusOne([4,3,2,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('digits = [0]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().plusOne([0])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('digits = [9]')
    print('Exception :')
    print('[1,0]')
    print('Output :')
    print(str(Solution().plusOne([9])))
    print()
    
    pass
# @lc main=end

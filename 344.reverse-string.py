# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#


# @lc tags=two-pointers;string

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
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1 
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = ["h","e","l","l","o"]')
    print('Exception :')
    print('["o","l","l","e","h"]')
    print('Output :')
    print(str(Solution().reverseString(["h","e","l","l","o"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = ["H","a","n","n","a","h"]')
    print('Exception :')
    print('["h","a","n","n","a","H"]')
    print('Output :')
    print(str(Solution().reverseString(["H","a","n","n","a","h"])))
    print()
    
    pass
# @lc main=end
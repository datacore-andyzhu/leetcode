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
        """ Solution 1: iterative """
        # left = 0
        # right = len(s) -1 
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        # return s
        """ Solution 2: Recursive """
        def helper(start, end, str):
            if not str or start>=end:
                return 
            helper(start+1, end-1, str)
            str[start], str[end] = str[end], str[start]
            
        helper(0, len(s)-1, s)

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

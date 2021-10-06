# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc tags=string

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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = collections.Counter(magazine)
        for char in ransomNote:
            if magazineDict.get(char, -1) == -1 or magazineDict.get(char, -1) <= 0:
                return False
            else:
                magazineDict[char] -= 1
        return True

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('ransomNote = "a", magazine = "b"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canConstruct("a","b")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('ransomNote = "aa", magazine = "ab"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canConstruct("aa","ab")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('ransomNote = "aa", magazine = "aab"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canConstruct("aa","aab")))
    print()
    
    pass
# @lc main=end

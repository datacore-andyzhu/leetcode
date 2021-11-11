# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc tags=stack;depth-first-search

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
    def decodeString(self, s: str) -> str:
        s = list(s)[::-1]

        def helper():
            ans = []
            k = 0
            while s:
                char = s.pop()
                if char.isalpha():
                    k = 0
                    ans.append(char)
                elif char.isnumeric():
                    k = k * 10 + int(char)
                elif char == '[':
                    res = helper()
                    ans.append(res * k)
                    k = 0
                elif char == ']':
                    return ''.join(ans)
            return ''.join(ans)

        return helper()
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "3[a]2[bc]"')
    print('Exception :')
    print('"aaabcbc"')
    print('Output :')
    print(str(Solution().decodeString("3[a]2[bc]")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "3[a2[c]]"')
    print('Exception :')
    print('"accaccacc"')
    print('Output :')
    print(str(Solution().decodeString("3[a2[c]]")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "2[abc]3[cd]ef"')
    print('Exception :')
    print('"abcabccdcdcdef"')
    print('Output :')
    print(str(Solution().decodeString("2[abc]3[cd]ef")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "abc3[cd]xyz"')
    print('Exception :')
    print('"abccdcdcdxyz"')
    print('Output :')
    print(str(Solution().decodeString("abc3[cd]xyz")))
    print()
    
    pass
# @lc main=end

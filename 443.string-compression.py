# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc tags=string

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
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        left = 0
        right = 0
        cnt = 0
        n = len(chars)
        while right < n:
            curr_char = chars[right]
            chars[left] = curr_char
            left += 1
            while right < n and chars[right] == curr_char:
                right += 1
                cnt += 1
            if cnt != 1:
                cnt_str = str(cnt)
                for i in range(len(cnt_str)):
                    chars[left] = cnt_str[i]
                    left += 1
            cnt = 0
        return left
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('chars = ["a","a","b","b","c","c","c"]')
    print('Exception :')
    print('Return 6, and the first 6 characters of the input array should be:["a","2","b","2","c","3"]')
    print('Output :')
    print(str(Solution().compress(["a","a","b","b","c","c","c"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('chars = ["a"]')
    print('Exception :')
    print('Return 1, and the first character of the input array should be: ["a"]')
    print('Output :')
    print(str(Solution().compress(["a"])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]')
    print('Exception :')
    print('Return 4, and the first 4 characters of the input array should be:["a","b","1","2"].')
    print('Output :')
    print(str(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('chars = ["a","a","a","b","b","a","a"]')
    print('Exception :')
    print('Return 6, and the first 6 characters of the input array should be:["a","3","b","2","a","2"].')
    print('Output :')
    print(str(Solution().compress(["a","a","a","b","b","a","a"])))
    print()
    
    pass
# @lc main=end

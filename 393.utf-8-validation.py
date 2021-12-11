# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
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
    def validUtf8(self, data: List[int]) -> bool:
        num_of_bytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            if num_of_bytes == 0:
                mask = 1 << 7
                while num & mask:
                    num_of_bytes += 1
                    mask = mask >> 1
                # if it is one-byte number
                if num_of_bytes == 0:
                    continue
                if num_of_bytes == 1 or num_of_bytes > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            num_of_bytes -= 1
        return num_of_bytes == 0
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('data = [197,130,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validUtf8([197, 130, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('data = [235,140,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validUtf8([235, 140, 4])))
    print()

    pass
# @lc main=end

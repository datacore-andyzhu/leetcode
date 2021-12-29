# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
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
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        num2Dict = Counter(changed)
        changed.sort()
        output = []
        for num in changed:
            if num not in num2Dict:
                continue
            double_num = num * 2
            if double_num not in num2Dict:
                return []
            output.append(num)
            num2Dict[num] -= 1
            if num2Dict[num] == 0:
                del num2Dict[num]
            num2Dict[double_num] -= 1
            if num2Dict[double_num] == 0:
                del num2Dict[double_num]
        return output
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('changed = [1,3,4,2,6,8]')
    print('Exception :')
    print('[1,3,4]')
    print('Output :')
    print(str(Solution().findOriginalArray([1, 3, 4, 2, 6, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('changed = [6,3,0,1]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findOriginalArray([6, 3, 0, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('changed = [1]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findOriginalArray([1])))
    print()

    pass
# @lc main=end

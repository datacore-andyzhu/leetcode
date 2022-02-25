# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#


# @lc tags=design;queue

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
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            elif bill == 20:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('bills = [5,5,5,10,20]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().lemonadeChange([5, 5, 5, 10, 20])))
    print()

    print('Example 2:')
    print('Input : ')
    print('bills = [5,5,10,10,20]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().lemonadeChange([5, 5, 10, 10, 20])))
    print()

    pass
# @lc main=end

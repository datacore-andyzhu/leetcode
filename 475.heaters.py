# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#


# @lc tags=binary-search

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
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        result = float('-inf')
        
        for house in houses:
            # the inner loop will cause the program TLE
            # min_heater = float('inf')
            # for heater in heaters:                
            #         min_heater = min(min_heater, abs(house-heater))
            left = 0
            right = n
            while left < right:
                mid = left + (right-left) // 2
                if house > heaters[mid]:
                    left = mid + 1
                else:
                    right = mid
            if right == 0:
                dist1 = float('inf')
            else:
                dist1 = abs(house - heaters[right-1])
            dist2 = abs(house-heaters[right]) if right != n else float('inf')

            result = max(result, min(dist1, dist2))
        return result
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('houses = [1,2,3], heaters = [2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findRadius([1, 2, 3], [2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('houses = [1,2,3,4], heaters = [1,4]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findRadius([1, 2, 3, 4], [1, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('houses = [1,5], heaters = [2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findRadius([1, 5], [2])))
    print()

    pass
# @lc main=end

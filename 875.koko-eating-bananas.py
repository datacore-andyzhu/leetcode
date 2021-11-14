# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc tags=two-pointers

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
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # consider this as a binary search problem with the
        # request to ask for the left edge of the target number
        # the target is the eat spead
        # define the ever increasing or ever decreasing function with
        # something as the input that make the function behave that way
        # in this case, the eating speed is input
        # and number of hours to finish all the bananas are the output
        # of the function
        def fx(piles, speed):
            hours = 0
            for i in range(len(piles)):
                hours += piles[i] // speed

                if piles[i] % speed != 0:
                    hours += 1
            return hours
        # start, end, mid is all about the eating speed
        start = 1
        end = 10**9 + 1
        while start < end:
            mid = start + (end - start) // 2
            if fx(piles, mid) == h:
                end = mid
            # this is ever decreasing function, so we need to be careful
            elif fx(piles, mid) < h:
                end = mid
            elif fx(piles, mid) > h:
                start = mid + 1
        return start

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('piles = [3,6,7,11], h = 8')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().minEatingSpeed([3, 6, 7, 11], 8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('piles = [30,11,23,4,20], h = 5')
    print('Exception :')
    print('30')
    print('Output :')
    print(str(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('piles = [30,11,23,4,20], h = 6')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6)))
    print()

    pass
# @lc main=end

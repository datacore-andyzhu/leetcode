# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
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
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # use the difference array trick to complete
        # build a diff array first, with value all equal to 0
        # the array length is n in this case
        diff_array = [0 for _ in range(n+1)]
        # loop through the bookings
        # mark from which flight, which is index of the n-array, to start add reservation
        # mark from which flight, to start to remove the reservation for that flight
        for i in range(len(bookings)):
            # bookings[i][0] start to add reservation bookings[i][2]
            diff_array[bookings[i][0]] += bookings[i][2]
            # bookings[i][1] start to remove reservation bookings[i][2]
            # from next flight number bookings[i][1] + 1 - 1
            # first plus 1 to indicate next gflight numer in array n
            # seond minus 1 is to balance for the 0 based index
            # because resevation is not added to all flights from 1 to n
            if bookings[i][1] + 1 <= n:
                diff_array[bookings[i][1] + 1] -= bookings[i][2]

        # finally rebuild the actual revervation from the reservation difference array
        results = [0 for _ in range(n+1)]
        results[1] = diff_array[1]
        for i in range(2, n+1):
            results[i] = results[i-1] + diff_array[i]
        return results[1:]
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5')
    print('Exception :')
    print('[10,55,45,25,25]')
    print('Output :')
    print(str(Solution().corpFlightBookings(
        [[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('bookings = [[1,2,10],[2,2,15]], n = 2')
    print('Exception :')
    print('[10,25]')
    print('Output :')
    print(str(Solution().corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2)))
    print()

    pass
# @lc main=end

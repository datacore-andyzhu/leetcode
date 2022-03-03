# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
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
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        index = 0

        while index + 2 < len(coordinates):
            value = self.check(
                coordinates[index], coordinates[index + 1], coordinates[index + 2])

            if not value:
                return False

            index += 1

        return True

    def check(self, a, b, c):
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        x3, y3 = c[0], c[1]

        return (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) == 0
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])))
    print()
    
    pass
# @lc main=end

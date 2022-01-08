# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#


# @lc tags=hash-table

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
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        answer = 0
        for i in range(len(points)):
            distance_dict = {}
            for j in range(len(points)):
                dist = pow(points[j][0]-points[i][0], 2) + \
                    pow(points[j][1]-points[i][1], 2)
                if dist in distance_dict:
                    distance_dict[dist] += 1
                else:
                    distance_dict[dist] = 1
            for _, r in distance_dict.items():
                if r > 1:
                    answer += r*(r-1)

        return answer
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[0,0],[1,0],[2,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[2,2],[3,3]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[1, 1], [2, 2], [3, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('points = [[1,1]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[1, 1]])))
    print()

    pass
# @lc main=end

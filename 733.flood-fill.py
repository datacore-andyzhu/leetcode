# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


# @lc tags=depth-first-search

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
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        direction_vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(image)
        n = len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(image, visited, sr, sc, originColor, newColor):
            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return
            if visited[sr][sc]:
                return
            if image[sr][sc] != originColor:
                return
            visited[sr][sc] = True

            for dir_x, dir_y in direction_vector:
                new_sr = sr + dir_x
                new_sc = sc + dir_y
                dfs(image, visited, new_sr, new_sc, originColor, newColor)
            image[sr][sc] = newColor
        originColor = image[sr][sc]
        dfs(image, visited, sr, sc, originColor, newColor)
        return image

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2')
    print('Exception :')
    print('[[2,2,2],[2,2,0],[2,0,1]]')
    print('Output :')
    print(str(Solution().floodFill(
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2')
    print('Exception :')
    print('[[2,2,2],[2,2,2]]')
    print('Output :')
    print(str(Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)))
    print()

    pass
# @lc main=end

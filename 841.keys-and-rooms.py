# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#


# @lc tags=Unknown

# @lc imports=start
import collections
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
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        bfs = collections.deque([0])

        while bfs:
            vertex = bfs.popleft()
            if visited[vertex] != True:
                visited[vertex] = True
                for neighbor in rooms[vertex]:
                    bfs.append(neighbor)

        for i in range(n):
            if visited[i] != True:
                return False
        return True

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rooms = [[1],[2],[3],[]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canVisitAllRooms([[1], [2], [3], []])))
    print()

    print('Example 2:')
    print('Input : ')
    print('rooms = [[1,3],[3,0,1],[2],[0]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])))
    print()

    pass
# @lc main=end

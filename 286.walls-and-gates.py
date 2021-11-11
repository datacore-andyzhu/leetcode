from typing import *
import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # we use BFS from the gate towards each empty room, instead of otherway around
        GATE = 0
        EMPTY = 2**31-1
        direction_vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque([])

        rows = len(rooms)
        if rows == 0:
            return
        cols = len(rooms[0])
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == GATE:
                    queue.append([row, col])

        while queue:
            node = queue.popleft()
            row = node[0]
            col = node[1]
            for dir_x, dir_y in direction_vector:
                new_row = row + dir_x
                new_col = col + dir_y
                if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or rooms[new_row][new_col] != EMPTY:
                    continue
                rooms[new_row][new_col] = rooms[row][col] + 1
                queue.append([new_row, new_col])

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        queue.append((start[0], start[1]))
        visited.add((start[0], start[1]))
        while queue:
            cell = queue.popleft()
            if cell[0] == destination[0] and cell[1] == destination[1]:
                return True
            for x, y in directions:
                new_x = cell[0] + x
                new_y = cell[1] + y
                while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0:
                    new_x += x
                    new_y += y
                # at this moment, the new_x and new_y is in invalid position
                # that's why we need back out one step
                new_x -= x
                new_y -= y
                if (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return False

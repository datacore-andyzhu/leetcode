class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dijkstra(maze, start, distance):
            pq = []
            heapq.heappush(pq, (0, start[0], start[1]))
            while pq:
                curr = heapq.heappop(pq)
                for _x, _y in directions:
                    count = 0
                    new_x = curr[1] + _x
                    new_y = curr[2] + _y
                    while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0:
                        new_x += _x
                        new_y += _y
                        count += 1
                    new_x -= _x
                    new_y -= _y
                    if distance[curr[1]][curr[2]] + count < distance[new_x][new_y]:
                        distance[new_x][new_y] = distance[curr[1]
                                                          ][curr[2]] + count
                        heapq.heappush(
                            pq, (distance[new_x][new_y], new_x, new_y))

        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        distance[start[0]][start[1]] = 0
        dijkstra(maze, start, distance)

        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float('inf') else -1

from typing import *
import collections
def minimumSemester(n: int, relations: List[List[int]]) -> int:
    adjList = {}
    inDegree = {}
    for i in range(1, n+1):
        adjList[i] = []
        inDegree[i] = 0
    
    for a, b in relations:
        adjList[a].append(b)
        inDegree[b] += 1

    completed = set()

    queue = collections.deque()
    steps = 0
    for key, value in inDegree.items():
        if value == 0:
            queue.append(key)
    
    if not queue:
        return -1
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            course = queue.popleft()
            completed.add(course)
            for _course in adjList[course]:
                inDegree[_course] -= 1
                if inDegree[_course] == 0 and _course not in completed:
                    queue.append(_course)
        steps += 1
    
    return steps if len(completed) == n else -1

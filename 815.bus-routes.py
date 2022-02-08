# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
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
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # use route as node, not use station as node
        if source == target:
            return 0
        # create dict use route value as key and other routes as value
        n = len(routes)
        new_routes = [set(r) for r in routes]
        routes_dict = defaultdict(list)
        for r1 in range(n):
            for r2 in range(n):
                if r2 != r1 and len(new_routes[r1].intersection(new_routes[r2])) > 0:
                    routes_dict[r1].append(r2)
        # src and tgt transformed into source/target routes
        source_routes = [r for r in range(n) if source in new_routes[r]]
        target_routes = set([r for r in range(n) if target in new_routes[r]])
        queue = source_routes
        len_queue = len(queue)
        buses = 1
        visited = set(source_routes)
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r = queue.pop(0)
                if r in target_routes:
                    return buses
                for neighbor in routes_dict[r]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            buses += 1
        return -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('routes = [[1,2,7],[3,6,7]], source = 1, target = 6')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numBusesToDestination([[1,2,7],[3,6,7]],1,6)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target= 12')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12)))
    print()
    
    pass
# @lc main=end

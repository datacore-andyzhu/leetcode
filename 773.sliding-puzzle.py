# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
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
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dst = '123450'
        src = ''
        zero_x = 0
        zero_y = 0
        m = len(board)
        n = len(board[0])

        def update(curr, x, y, new_x, new_y):
            curr_list = list(curr)
            curr_list[x*n+y], curr_list[new_x*n +
                                        new_y] = curr_list[new_x*n+new_y], curr_list[x*n+y]
            return ''.join(curr_list)

        def bfs(src, x, y, dst):
            # we use the src string plus zero's location as node of the queue
            queue = deque()
            # steps = {}
            # we use a dictioanry to store not only the visited set but also the steps
            # steps[src] = 0
            visited = set()
            queue.append((src, x, y))
            steps = 0
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    string, x, y = queue.popleft()
                    # print('old string: ', string)
                    if string in visited:
                        continue
                    visited.add(string)
                    if string == dst:
                        return steps
                    for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= new_x < m and 0 <= new_y < n:
                            new_string = update(string, x, y, new_x, new_y)
                            # print('new string: ', new_string)
                            if new_string in visited:
                                continue
                            new_node = (new_string, new_x, new_y)
                            queue.append(new_node)
                steps += 1
            return -1

        # build the src string and record where the zero location at the start
        for i in range(m):
            for j in range(n):
                src += str(board[i][j])
                if board[i][j] == 0:
                    zero_x = i
                    zero_y = j

        ans = bfs(src, zero_x, zero_y, dst)
        return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = [[1,2,3],[4,0,5]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().slidingPuzzle([[1,2,3],[4,0,5]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('board = [[1,2,3],[5,4,0]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().slidingPuzzle([[1,2,3],[5,4,0]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('board = [[4,1,2],[5,0,3]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().slidingPuzzle([[4,1,2],[5,0,3]])))
    print()
    
    pass
# @lc main=end

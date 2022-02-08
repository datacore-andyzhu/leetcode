# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#


# @lc tags=math;dynamic-programming;minimax

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
import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if board[0][0] != -1:
            return -1

        def idx2rc(idx):
            r, c = (idx-1) // n, (idx-1) % n
            if r % 2 == 1:
                c = n-1-c
            return n-1-r, c
        visited = set()
        queue = collections.deque()

        queue.append(1)
        steps = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                cell_idx = queue.popleft()
                if cell_idx in visited:
                    continue
                visited.add(cell_idx)
                for i in range(1, 6+1):
                    new_cell_idx = cell_idx + i
                    if new_cell_idx > n*n:
                        break
                    x_nxt, y_nxt = idx2rc(new_cell_idx)
                    if board[x_nxt][y_nxt] > 0:
                        new_cell_idx = board[x_nxt][y_nxt]
                    if new_cell_idx == n*n:
                        return steps
                    if new_cell_idx not in visited:
                        queue.append(new_cell_idx)
            steps += 1
        return -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board =[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('board = [[-1,-1],[-1,3]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().snakesAndLadders([[-1,-1],[-1,3]])))
    print()
    
    pass
# @lc main=end

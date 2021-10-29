# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
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
    def findTheWinner(self, n: int, k: int) -> int:
        """ Solution 1 """
        # friends_queue = collections.deque([])
        # for i in range(1, n+1):
        #     friends_queue.append(i)
        # i = 1
        # while len(friends_queue) != 1:
            
        #     friend = friends_queue.popleft()
        #     if i != k:
        #         friends_queue.append(friend)
        #         i = i+1
        #     else:
        #         i = 1
        # return friends_queue[-1]

        """ Solution 2 """
        index = 0
        friends = [i for i in range(1, n+1)]

        while (len(friends) > 1):
            if (index + k - 1) >= n:
                index = (index + k - 1) % n
            else:
                index += (k-1)
            friends.pop(index)
            n -= 1

        return friends[0]
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, k = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findTheWinner(5,2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 6, k = 5')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findTheWinner(6,5)))
    print()
    
    pass
# @lc main=end

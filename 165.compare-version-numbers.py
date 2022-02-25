# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#


# @lc tags=string

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
    
    def get_next_chunk(self, version, n, p):
            # if pointer is set to the end of string
            # return 0
        if p > n-1:
            return 0, p

        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        # retrieve the chunk
        i = int(version[p:p_end]) if p_end != n-1 else int(version[p:n])
        # find the beginning of next chunk
        p = p_end + 1
        return i, p

    def compareVersion(self, version1: str, version2: str) -> int:
        m = len(version1)
        n = len(version2)

        p1 = p2 = 0
        while p1 < m or p2 < n:
            i1, p1 = self.get_next_chunk(version1, m, p1)
            i2, p2 = self.get_next_chunk(version2, n, p2)
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('version1 = "1.01", version2 = "1.001"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().compareVersion("1.01","1.001")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('version1 = "1.0", version2 = "1.0.0"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().compareVersion("1.0","1.0.0")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('version1 = "0.1", version2 = "1.1"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().compareVersion("0.1","1.1")))
    print()
    
    pass
# @lc main=end

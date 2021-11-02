# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#


# @lc tags=hash-table;heap

# @lc imports=start
import collections
import heapq
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
    def frequencySort(self, s: str) -> str:
        hash_table = collections.defaultdict(int)
        myheap = []
        result = ''
        for char in s:
            hash_table[char] -= 1
        for key, value in hash_table.items():
            heappush(myheap, (value, key))

        while len(myheap):
            times, char = heappop(myheap)
            result += char*(times*-1)
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "tree"')
    print('Exception :')
    print('"eert"')
    print('Output :')
    print(str(Solution().frequencySort("tree")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cccaaa"')
    print('Exception :')
    print('"aaaccc"')
    print('Output :')
    print(str(Solution().frequencySort("cccaaa")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "Aabb"')
    print('Exception :')
    print('"bbAa"')
    print('Output :')
    print(str(Solution().frequencySort("Aabb")))
    print()

    pass
# @lc main=end

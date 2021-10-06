# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc tags=hash-table;string

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
    def firstUniqChar(self, s: str) -> int:
        # use a array table with 26 charster position to solve this
        # hashTable = [0]*26
        # for char in s:
        #     hashTable[ord(char)-ord('a')] += 1
        # for i in range(len(s)):
        #     if hashTable[ord(s[i])-ord('a')] == 1:
        #         return i
        # return -1

        # use hash table and return min value of the hashtable
        hashTable = {}
        seen = set()
        for i in range(len(s)):

            if hashTable.get(s[i], -1) == -1 and s[i] not in seen:
                hashTable[s[i]] = i
                seen.add(s[i])
            elif hashTable.get(s[i], -1) != -1 and s[i] in seen:
                hashTable.pop(s[i])
        if hashTable:
            return min(hashTable.values())
        else:
            return -1

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "leetcode"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().firstUniqChar("leetcode")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "loveleetcode"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().firstUniqChar("loveleetcode")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "aabb"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().firstUniqChar("aabb")))
    print()

    pass
# @lc main=end

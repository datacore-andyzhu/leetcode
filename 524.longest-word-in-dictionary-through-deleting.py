# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#


# @lc tags=two-pointers;sort

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
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """ Solution 1 """
        # first sort the dictionary by len of word and then by alphabet
        dictionary.sort(key=lambda x: (-len(x), x))
        
        n = len(s)
        # then for each word, search the string and see if they can 'match'
        for word in dictionary:
            m = len(word)
            i = 0
            j = 0
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == m:
                return word
        return ''
        """ SOlution 2: without osrting the dictionary """
        def isSubsequence(target, source):
            i = 0
            j = 0
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(target)
        max_str = ''
        for word in dictionary:
            if isSubsequence(word, s):
                if len(word) > len(max_str) or (len(word) == len(max_str) and word < max_str):
                    max_str = word
        return max_str
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]')
    print('Exception :')
    print('"apple"')
    print('Output :')
    print(str(Solution().findLongestWord("abpcplea",["ale","apple","monkey","plea"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "abpcplea", dictionary = ["a","b","c"]')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().findLongestWord("abpcplea",["a","b","c"])))
    print()
    
    pass
# @lc main=end

# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#


# @lc tags=array;string;backtracking;breadth-first-search

# @lc imports=start
import collections
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
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def creatWordGraph(wordLists):
            bucket = defaultdict(list)
            for word in wordLists:
                for i in range(len(word)):
                    bucket_key = word[:i]+'_'+word[i+1:]
                    bucket[bucket_key].append(word)
            graph = defaultdict(list)
            for bucket_key in bucket:
                for word1 in bucket[bucket_key]:
                    for word2 in bucket[bucket_key]:
                        if word2 != word1:
                            graph[word1].append(word2)
            return graph
        if endWord not in wordList:
            return []
        if beginWord == endWord:
            return [beginWord]

        visited = set()
        wordset = set(wordList)
        wordset.add(beginWord)
        graph = creatWordGraph(wordset)

        results = []
        queue = collections.deque([[beginWord]])
        visited.add(beginWord)
        while queue:
            level_size = len(queue)
            aux_set = set()
            for _ in range(level_size):
                curr_path = queue.popleft()
                curr_word = curr_path[-1]

                if curr_word == endWord:
                    results.append(curr_path[:])
                for nextword in graph[curr_word]:
                    if nextword not in visited:
                        aux_set.add(nextword)
                        queue.append(curr_path[:] + [nextword])
            visited.update(aux_set)
        return results
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log","cog"]')
    print('Exception :')
    print('[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]')
    print('Output :')
    print(str(Solution().findLadders("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log"]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findLadders("hit", "cog",
          ["hot", "dot", "dog", "lot", "log"])))
    print()

    pass
# @lc main=end

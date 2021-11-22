# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#


# @lc tags=breadth-first-search

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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ Using bucket list """
        # def creatWordBucket(wordLists):
        #     bucket = defaultdict(list)
        #     for word in wordLists:
        #         for i in range(len(word)):
        #             bucket[word[:i]+'_'+word[i+1:]].append(word)
        #     return bucket
        # if endWord not in wordList:
        #     return 0
        # wordset = set(wordList)
        # wordset.add(beginWord)
        # bucket = creatWordBucket(wordset)
        # visited = set()
        # result = []
        # queue = collections.deque([])
        # queue.append([beginWord])
        # while queue:
        #     level_size = len(queue)
        #     for _ in range(level_size):
        #         curr_path = queue.popleft()
        #         last_word = curr_path[-1]
        #         visited.add(last_word)
        #         if last_word == endWord:
        #             result.append(curr_path[:])
        #         else:
        #             for i in range(len(beginWord)):
        #                 for next in bucket[last_word[:i]+'_'+last_word[i+1:]]:
        #                     if next not in visited:
        #                         queue.append(curr_path[:]+[next])

        # if result:
        #     return len(result[0])
        # else:
        #     return 0

        """ using graph instead of bucket list """
        # def creatWordGraph(wordLists):
        #     bucket = defaultdict(list)
        #     for word in wordLists:
        #         for i in range(len(word)):
        #             bucket_key = word[:i]+'_'+word[i+1:]
        #             bucket[bucket_key].append(word)
        #     graph = defaultdict(list)
        #     for bucket_key in bucket:
        #         for word1 in bucket[bucket_key]:
        #             for word2 in bucket[bucket_key]:
        #                 if word2 != word1:
        #                     graph[word1].append(word2)
        #     return graph
        # if endWord not in wordList:
        #     return 0
        # wordset = set(wordList)
        # wordset.add(beginWord)
        # graph = creatWordGraph(wordset)
        # visited = set()
        # result = []
        # queue = collections.deque([[beginWord]])
        # visited.add(beginWord)
        # while queue:
        #     level_size = len(queue)
        #     for _ in range(level_size):
        #         curr_path = queue.popleft()
        #         last_word = curr_path[-1]
        #         visited.add(last_word)
        #         if last_word == endWord:
        #             result.append(curr_path[:])
        #         for neighbor in graph[last_word]:
        #             if neighbor not in visited:
        #                 queue.append(curr_path[:] + [neighbor])
        # if result:
        #     return len(result[0])
        # else:
        #     return 0
        """ Solution 3: using the prev dictionary to record the visisted path"""
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
            return 0
        wordset = set(wordList)
        wordset.add(beginWord)
        graph = creatWordGraph(wordset)
        visited = set()
        result = []
        queue = collections.deque([beginWord])
        visited.add(beginWord)
        prev = {}
        while queue:
            level_size = len(queue)
            for _ in range(level_size):                
                last_word = queue.popleft()
                
                if last_word == endWord:
                    break
                for neighbor in graph[last_word]:
                    if neighbor not in visited:
                        visited.add(neighbor)                     
                        queue.append(neighbor)
                        prev[neighbor] = last_word
        if endWord not in prev:
            return 0
        pre = endWord
        while pre != beginWord:
            result.append(pre)
            pre = prev[pre]
        result.append(pre) # add the beginWord
        return len(result[::-1])            
        
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log","cog"]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"])))
    print()

    pass
# @lc main=end

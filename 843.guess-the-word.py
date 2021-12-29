# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
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
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        """ Solution 1 """

    #     N = len(wordlist)
    #     self.H = [[sum(a == b for a, b in zip(wordlist[i], wordlist[j]))
    #                for j in range(N)] for i in range(N)]

    #     possible, path = range(N), ()
    #     while possible:
    #         guess = self.solve(possible, path)
    #         matches = master.guess(wordlist[guess])
    #         if matches == len(wordlist[0]):
    #             return
    #         possible = [j for j in possible if self.H[guess][j] == matches]
    #         path = path + (guess,)

    # def solve(self, possible, path=()):
    #     if len(possible) <= 2:
    #         return possible[0]

    #     ansgrp, ansguess = possible, None
    #     for guess, row in enumerate(self.H):
    #         if guess not in path:
    #             groups = [[] for _ in range(7)]
    #             for j in possible:
    #                 if j != guess:
    #                     groups[row[j]].append(j)
    #             maxgroup = max(groups, key=len)
    #             if len(maxgroup) < len(ansgrp):
    #                 ansgrp, ansguess = maxgroup, guess

    #     return ansguess
        """ Solution 2 """
        for i in range(10):
            init_word = wordlist[random.randint(0,len(wordlist) - 1)]
            pat = master.guess(init_word)
            if pat == 6:
                return
            temp = []
            for cur_word in wordlist:
                cnt = 0
                for k in range(6):
                    if cur_word[k] == init_word[k]:
                        cnt += 1
                    if cnt > pat:
                        break
                if cnt == pat:
                    temp.append(cur_word)
            wordlist = temp
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"],numguesses = 10')
    print('Exception :')
    print('You guessed the secret word correctly.')
    print('Output :')
    print(str(Solution().findSecretWord(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10')
    print('Exception :')
    print('You guessed the secret word correctly.')
    print('Output :')
    print(str(Solution().findSecretWord(error, error)))
    print()

    pass
# @lc main=end

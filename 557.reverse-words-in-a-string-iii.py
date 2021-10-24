# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
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
    def reverseWords(self, s: str) -> str:
        wordlist = s.split(' ')
        result = []

        def reverse(s):
            result = ''
            for i in range(len(s)-1, -1, -1):
                result += s[i]
            return result

        for word in wordlist:
            new_word = reverse(word)
            result.append(new_word)

        return ' '.join(result)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Let's take LeetCode contest"')
    print('Exception :')
    print('"s'teL ekat edoCteeL tsetnoc"')
    print('Output :')
    print(str(Solution().reverseWords("Let's take LeetCode contest")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "God Ding"')
    print('Exception :')
    print('"doG gniD"')
    print('Output :')
    print(str(Solution().reverseWords("God Ding")))
    print()

    pass
# @lc main=end

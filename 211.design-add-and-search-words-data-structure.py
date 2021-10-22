# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc tags=backtracking;design;trie

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


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_finished = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.word_finished = True

    def search(self, word: str) -> bool:
        node = self.root
        # if we meet a condition which is an empty dictionay
        # return False
        if node.children == []:
            return False

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node.children:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for _node in node.children.values():
                            if search_in_node(word[i + 1:], _node):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node.children[ch]
            return node.word_finished

        return search_in_node(word, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
# @lc main=start
if __name__ == '__main__':
    pass
# @lc main=end

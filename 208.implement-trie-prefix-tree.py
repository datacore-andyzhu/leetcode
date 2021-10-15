# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc tags=design;trie

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
    def __init__(self, char='*') -> None:
        self.char = char
        self.children = {}
        self.counter = 1
        self.word_finished = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        found_in_child = False
        for ch in word:
            if node.children.get(ch, 0) == 0:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
            else:
                node = node.children[ch]
        node.word_finished = True

    def search(self, word: str) -> bool:
        node = self.root
        # if it is an empty Trie
        if not node.children:
            return False

        for ch in word:
            if ch not in node.children:

                return False
            else:
                node = node.children[ch]

        if node.word_finished:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        # if it is an empty Trie
        if not node.children:
            return False

        for ch in prefix:
            if ch not in node.children:

                return False
            else:
                node = node.children[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end

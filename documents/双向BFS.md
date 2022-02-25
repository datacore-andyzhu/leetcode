双向BFS

### 127. 单词接龙

```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)

            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        queue.append((next_word, length+1))
                        wordList.remove(next_word)
        return 0

```



```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0

```

### 433. 最小基因变化

```python
class Solution:
    def minMutation(self, start, end, bank):
        queue = [(start, 0)]
        bank = set(bank)
        while queue:
            cur, count = queue.pop(0)
            if cur == end: return count
            for i in range(0, len(start)):
                for ch in ['A', 'C', 'G', 'T']:
                    new = cur[0:i] + ch + cur[i+1:]
                    if new in bank:
                        queue.append((new, count+1))
                        bank.remove(new)
        return -1

```

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1

```


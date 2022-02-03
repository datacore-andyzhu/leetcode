from collections import *
def alientDict(wordList):
    adj_list = defaultdict(set)
    in_degree = Counter({c:0 for word in wordList for c in word})

    for firstword, secondword in zip(wordList, wordList[1:]):
        for c, d in zip(firstword, secondword):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else:
            if len(secondword) < len(firstword):
                return ''
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        letter = queue.popleft()
        output.append(letter)
        for neighbor in adj_list[letter]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # return output
    if len(output) < len(in_degree):
        return ''
    return ''.join(output)

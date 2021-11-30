from collections import defaultdict


def groupString(strings):
    group_dict = defaultdict(list)
    for word in strings:
        # creating tuple to recognize the pattern of the relationship among char in the word
        # the distiance between second char with 1st char, 3rd with 2dn, so on
        code = tuple([ (ord(word[x+1]) - ord(word[x]))%26 for x in range(len(word)-1) ])
        if code in group_dict:
            group_dict[code].append(word)
        else:
            group_dict[code] = [word]
    return list(group_dict.values())


print(groupString(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # for idx, val in enumerate(spaces):
        #     s = s[:val+idx] + ' ' + s[idx+val:]
        # return s

        # new_str = ''
        # i = j = 0
        # while i < len(s):
        #     if j < len(spaces) and spaces[j] == i:
        #         new_str += ' '
        #         j += 1
        #     new_str += s[i]
        #     i += 1
        # return new_str
        newst = ""
        spaces = set(spaces)
        for i, val in enumerate(s):
            if i in spaces:
                newst += " "
            newst += val

        return newst

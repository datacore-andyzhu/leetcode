class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        distinct = set()
        for string in dict:
            for i in range(len(string)):
                temp = string[:i] + '.' + string[i+1:]
                if temp in distinct:
                    return True
                distinct.add(temp)
        return False

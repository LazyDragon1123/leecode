class Solution:
    def firstUniqChar(self, s:str) -> int:
        dic = {}
        dic_unique = {}
        for ind, char in enumerate(s):
            if dic_unique.get(char) is None:
                dic[char] = ind
                dic_unique[char] = 1
                continue
            else:
                if dic.get(char) is not None:
                    dic.pop(char)
                    continue
        print(dic)
        return list(dic.values())[0] if len(list(dic.values())) > 0 else -1

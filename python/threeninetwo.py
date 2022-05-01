from collections import deque


class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        if len(s) == 0:
            return True
        de = deque([c for c in s])
        for char in t:
            i = de[0]
            if char == i:
                de.popleft()
                if len(de) == 0:
                    return True
        return False

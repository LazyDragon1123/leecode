
def converter(fs,ns):
    if fs == 'I':
        if ns == 'V' or ns == 'X':
            return -1
        else:
            return 1
    elif fs == 'V':
        return 5
    elif fs == 'X':
        if ns == "L" or ns == 'C':
            return -10
        else:
            return 10
        
    elif fs == 'L':
        return 50
    
    elif fs == 'C':
        if ns == 'D' or ns == 'M':
            return -100
        else:
            return 100
        
    elif fs == 'D':
        return 500
    
    elif fs == 'M':
        return 1000
    else:
        return None

class Solution:
    def romanToInt(self, s:str) -> int:
        ans = 0
        for ind in range(len(s)-1):
            ans += converter(s[ind], s[ind+1])
        ans += converter(s[-1], "None")
        return ans

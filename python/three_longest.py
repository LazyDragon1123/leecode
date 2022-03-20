class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        tmpset = set()
        tmpset.add(s[0])
        best = 1
        stind = 0
        enind = 1
        while enind < len(s):
            ind = enind
            if s[ind] in tmpset:
                if best < len(tmpset):
                    best = len(tmpset)
                tmpset.remove(s[stind])
                stind += 1
                enind = max(enind, stind)
            else:
                tmpset.add(s[ind])
                enind += 1
            if ind == len(s) - 1:
                if best < len(tmpset):
                    best = len(tmpset)
        return best
            
            
# sliing window
        

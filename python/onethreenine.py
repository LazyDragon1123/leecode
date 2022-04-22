# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         if len(s) == 0:
#             return True
#         for idx in range(1, len(wordDict) + 1):
#             if s[:idx] in wordDict:
#                 ret = self.wordBreak(s[idx:], wordDict)
#                 if ret is True:
#                     return True
#         return False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
    
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for idx in range(1, len(s)+1):
            for w in wordDict:
                if -idx + len(w) == 0 and s[-idx:] == w:
                    dp[-idx - 1] = dp[-1 -idx+len(w)]
                elif -idx + len(w) < 0 and s[-idx:-idx+len(w)] == w:
                    dp[-idx - 1] = dp[-1 -idx+len(w)]
                if dp[-idx - 1]:
                    break
        return dp[0]

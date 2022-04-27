import numpy as np

# def dfs(amount, coins, caches):
#     if amount in coins:
#         return 1
#     if min(coins) > amount:
#         return -1
#     if caches.get(amount) is not None:
#         return caches[amount]
    
#     cand = np.array([dfs(amount - coin, coins, caches) for coin in coins])
    
#     if np.where(cand == -1, True, False).all():
#         caches[amount] = -1
#         return -1
#     else:
#         caches[amount] = min(cand[np.where(cand == -1, False, True)])+1 
#         return caches[amount]

def dp(amount, coins, caches):
    if caches.get(amount) is not None:
        return caches[amount]
    if amount in coins:
        return 1
    if min(coins) > amount:
        return -1
    
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        dp[0] = 0
        mincoins = min(coins)
        for i in range(1, amount+1):
            if i < mincoins:
                dp[i] = -1
                continue
            else:
                cands = np.array([dp[i-j] + 1 for j in coins if i - j >= 0])
                if np.where(cands==0, True, False).all():
                    dp[i] = -1
                else:
                    dp[i] = min(cands[np.where(cands==0, False, True)])
        return dp[amount]

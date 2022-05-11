import numpy as np

def days(piles, k):
    ret = 0
    for pile in piles:
        ret += int(np.ceil(pile / k))
    return ret

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force 
        # k = 1
        # while True:
        #     if days(piles, k) <= h:
        #         return k
        #         break
        #     else:
        #         k += 1
        # binary search strategy
        mi = 1
        ma = max(piles)
        mid = (mi + ma) // 2
        while not ((mi + 1) >= ma):
            if days(piles, mid) > h:
                mi = mid
                mid = (mi + ma) //2
            else:
                ma = mid
                mid = (mi + ma) //2
        for k in range(mi, ma +1):
            if days(piles, k) <=h:
                return k
                
            
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        pmin = min(prices[:2])
        maxprofit = prices[1] - pmin
        if len(prices) == 2:
            return max(maxprofit, 0)
        for pr in prices[2:]:
            maxprofit = max(maxprofit, pr - pmin)
            print(maxprofit)
            pmin = min(pmin, pr)

        return max(maxprofit, 0)
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for ind in range(len(prices)-1):
            if prices[ind] < prices[ind + 1]:
                profit += prices[ind + 1] - prices[ind]

        return profit           

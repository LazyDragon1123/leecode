class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        for c in cost[2:]:
            dp.append(min(dp[-2], dp[-1]) + c)
        return dp[-1]

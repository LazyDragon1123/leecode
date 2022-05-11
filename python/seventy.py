class Solution:
    def climbStairs(self, n: int) -> int:
        ret = 0
        dp = []
        dp.append(1)
        dp.append(1)
        for _ in range(1,n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force
        num = len(nums)
        if num == 1:
            return 1
        dp = []
        dp.append(1)
        for i in range(num - 2, -1, -1):
            tmp = 1
            for j in range(i+1, num):
                if nums[i] < nums[j]:
                    if tmp < 1 + dp[num - 1 - j]:
                        tmp = 1 + dp[num - 1 - j]
                        continue
            dp.append(tmp)
            
        return max(dp)
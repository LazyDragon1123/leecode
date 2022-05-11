class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) =< 2:
            return max(nums)
        dp = [nums[0], nums[1]]
        for idx in range(2, len(nums)):
            dp.append(max(dp[-2] + nums[idx], dp[-1]))
        return dp[-1]
        
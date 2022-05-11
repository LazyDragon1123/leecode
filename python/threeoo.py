class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## brute force
        # cand = [nums[0]]
        # for i in range(len(nums)):
        #     tmp = [nums[i]]
        #     for j in range( i+ 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             tmp.append(nums[j])
        #     if len(cand) < len(tmp):
        #         cand = tmp
        # return len(cand)
        # dp
        # dp = []
        # dp.append(1)

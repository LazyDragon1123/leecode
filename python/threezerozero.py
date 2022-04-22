import numpy as np


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        maxsubs = np.ones(len(nums))
        lastid = len(nums) - 1
        for ind in range(len(nums) - 1):
            subject = nums[lastid - ind - 1]
            tmp = [1]
            for j in range(ind + 1):
                if nums[lastid - j] > subject:
                    tmp.append(1 + maxsubs[lastid - j])
                else:
                    continue
            maxsubs[lastid - ind - 1] = max(tmp)
        return int(max(maxsubs))
        

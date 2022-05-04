# rule: l_max < sum of the others
from itertools import combinations


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # brute force
        # ret = 0
        # for i, j, k in combinations(nums, 3):
        #     max_l = max(i,j,k)
        #     if max_l < i+j+k - max_l:
        #         ret += 1
        # return ret
        # sort
        ret = 0
        sortnums = sorted(nums)[::-1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if sortnums[i] < sortnums[j] + sortnums[k]:
                        ret += len(nums) - k
                        break
        return ret

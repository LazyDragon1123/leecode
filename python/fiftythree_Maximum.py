from operator import ne


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if nums[0] < 0:
            edgearr = nums[1]
            nedgearr = nums[0]
        else:
            edgearr = sum(nums[:2])
            nedgearr = nums[0]
        # if len(nums) == 2:
        #     return max(edgearr,nedgearr)
        for next in nums[2:]:

            nedgearr = max(edgearr, nedgearr)
            edgearr = max(edgearr + next, next)

        return max(edgearr, nedgearr)
                
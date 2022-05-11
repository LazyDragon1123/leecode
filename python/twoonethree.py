class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp_s_w = [nums[0], 0]
        dp_s_wo = [nums[0], nums[0]]
        dp_ns_w = [0, nums[1]]
        dp_ns_wo = [0, 0]
        for i in range(2, n):
            dum = dp_s_w[-1]
            dp_s_w.append(dp_s_wo[-1] + nums[i]) 
            dp_s_wo.append(max(dum, dp_s_wo[-1]))
            dum = dp_ns_w[-1]             
            dp_ns_w.append(dp_ns_wo[-1] + nums[i]) 
            dp_ns_wo.append(max(dum, dp_ns_wo[-1]))
        return max(dp_s_wo[-1], dp_ns_w[-1], dp_ns_wo[-1])
                           
            
        
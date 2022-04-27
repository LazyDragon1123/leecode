class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_tail = nums[0]
        max_n_tail = 0
        for n in nums[1:]:
            max_tail_ = max_tail
            max_n_tail_ = max_n_tail
            max_n_tail = max(max_n_tail_, max_tail_)
            max_tail = max_n_tail_ + n
        return max(max_n_tail, max_tail)

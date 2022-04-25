class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        r = 0
        l = 1
        ans = float('inf')
        while (l<=len(nums) or l==r):
            sum_ = sum(nums[r:l])
            if sum_ >= target:
                if ans > (l-r):
                    ans = l-r
                r += 1
            else:
                l += 1
        return ans

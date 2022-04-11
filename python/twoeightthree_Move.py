class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for id in enumerate(nums):
            if len(nums) <2:
                return nums
            cout = 0
            nx = 0
            while cout < len(nums):
                cout += 1
                if nums[nx] == 0:
                    nums.pop(nx)
                    nums.append(0)
                else:
                    nx += 1
                    
            return nums

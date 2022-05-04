class Solution:
    def search(self, nums: List[int], target:int) -> int:
        left = len(nums) - 1
        right = 0
        while left >= right:
            mid = right + (left - right) //2
            if nums[right] > target or nums[left] < target:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid + 1
                continue
            else:
                left = mid - 1
                continue
        if nums[left] == target:
            return left
        return -1
            
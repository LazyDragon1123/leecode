def binary(arr):
    print(arr)
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    rtail = arr[mid - 1]
    lhead = arr[mid]
    if rtail > lhead:
        return lhead
    else:
        ret = binary(arr[:mid])
        ret_ = binary(arr[mid:])
        return ret if ret is not None else ret_

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        return binary(nums)

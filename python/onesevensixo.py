import numpy as np
def ops(nums, mi, cap):
    ret = 0 
    for num in nums:
        if num <= mi:
            continue
        ret += (int(np.ceil(num / mi)) -1)
        if ret > cap:
            return float('inf')
    return ret

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        mi = 1
        ma = max(nums)
        mid = (mi + ma) //2
        while not (mi + 1 >= ma):
            if ops(nums, mid, maxOperations) <= maxOperations:
                ma = mid
                mid = (mi + ma) //2
            else:
                mi = mid
                mid = (mi + ma) //2
                
        for k in range(mi, ma + 1):
            if ops(nums, k, maxOperations) <= maxOperations:
                return k
        
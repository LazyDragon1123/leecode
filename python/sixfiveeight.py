import numpy as np

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_arr = [abs(x - i) for i in arr]
        indices = np.argsort(abs_arr)
        min_ind = np.where(indices==0)[0][0]
        i = 1
        j = -1
        ret_ind = [min_ind]
        while len(ret_ind) < k:
            if min_ind + i >= len(arr):
                right = float('inf')
            if min_ind + j < 0:
                left = float('inf')
            if right < left:
                ret_ind.append(min_ind + i)
                i += 1
            else:
                ret_ind.append(min_ind + j)
                j -= 1
        ret_ind = sorted(ret_ind)
        return arr[ret_ind]
            
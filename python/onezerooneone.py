import numpy as np


def cal_D(weights, capw):
    day = 0
    cap = capw
    for w in weights:
        if w <= cap:
            cap -= w
        else:
            day += 1
            cap = capw - w
    return day+1



class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        large = sum(weights) # one day
        small = max(weights)
        mid = int((large + small) / 2)
        while mid:
            if cal_D(weights, mid) > days:
                small = mid
                mid = int(np.mean([large, small]))
            else:
                large = mid
                mid = int(np.mean([large, small]))
            if mid == small and mid == large:
                return mid
            if small == mid and (mid + 1 == large):
                if cal_D(weights, mid) <= days:
                    return mid
                else:
                    return large
        return mid

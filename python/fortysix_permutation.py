import copy

import numpy as np


def generate(res, cand, left):
    if len(left) == 0:
        res.append(cand)
        return
    for ind, num in enumerate(left):
        generate(res, list(np.append(np.array(cand), num)), list(np.append(np.array(left)[:ind], np.array(left)[ind+1:])))

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        left = nums
        generate(res, [], left)
        return res

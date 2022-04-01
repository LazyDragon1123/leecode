import numpy as np


def generate(res, cands, remain, arr):
    if remain == 0:
        res.append(arr)
        return
    
    for ind, cand in enumerate(cands):
        if cand > remain:
            continue
        else:
            generate(res, cands[ind:], remain - cand, np.append(arr, cand))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        generate(res, candidates, target, np.array([]))
        return res


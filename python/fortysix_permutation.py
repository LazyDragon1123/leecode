import copy


def generate(res, cand, left):
    if len(left) == 0:
        res.append(cand)
        return
    left_ = []
    for ind, num in enumerate(left):
        left_.extend(left[:ind])
        left_.extend(left[ind:])
        cand.append(num)
        generate(res, cand, left_)
        cand.pop(-1)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        generate(ret, [], nums)
        return ret

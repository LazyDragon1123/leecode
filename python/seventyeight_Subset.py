import numpy as np


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        
        for num in nums:
            new = [re + [num] for re in res]
            res.extend(new)
        
        return res

import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if dic.get(num) is None:
                dic[num] = 1
            else:
                dic[num] += 1
        sortarg = np.argsort(np.array(list(dic.values())))[::-1]
        return np.array(list(dic.keys()))[sortarg][:k]
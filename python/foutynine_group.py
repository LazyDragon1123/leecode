from signal import strsignal

import numpy as np


def convert_base(string):
    dic = {}
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            sort = ''.join(sorted(string))
            if dic.get(sort) is None:
                dic[sort] = {}
            if dic[sort].get(string) is None:
                dic[sort][string] = 1
            else:
                dic[sort][string] += 1
        ans = []
        for s, dicv in dic.items():
            tmp = []
            for k in dicv.keys():
                tmp.append(k)
            ans.append(tmp)
            
        return ans

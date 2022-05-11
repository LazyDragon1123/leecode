import numpy as np
# from math import product

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # #brute force
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if product(nums[i:j+1]) > 0 and ans < j+1 - i:
        #             ans = j+1-i
        #         continue
        # return ans
        
        #make disconnected by zero and count negative
        
        #dp of negative andpositive
        dpn = [0]
        dpp = [0]
        for i in nums:
            if i > 0:
                dpp.append(dpp[-1] + 1)
                if dpn[-1] != 0:
                    dpn.append(dpn[-1] + 1)
                else:
                    dpn.append(0)
            elif i<0:
                dum = dpp[-1]
                if dpn[-1] != 0:
                    dpp.append(dpn[-1] + 1)
                else:
                    dpp.append(0)
                dpn.append(dum + 1) 
            else:
                dpp.append(0)
                dpn.append(0)
        return max(dpp)
            
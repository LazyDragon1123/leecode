

from multiprocessing import cpu_count


class Solution:
    def search(self, nums: List[int], target:int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: 
                return -1
        # find rotate index
        rotarr = nums
        stind = 0
        flag = True
        while len(rotarr) > 1:
            ind = len(rotarr) // 2
            if rotarr[ind] > rotarr[-1]:
                rotarr = rotarr[ind:]
                stind += stind + ind
                flag = False
                continue
            else:
                rotarr = rotarr[:ind]
                
                continue
        if flag:
            rotarr = nums
            rotind = 0
        else:
            stind += 1
            rotarr = nums[stind:]
            rotarr.extend(nums[:stind])
            rotind = stind
        
        stind = 0
        while len(rotarr) > 1:
            ind = len(rotarr) // 2
            if rotarr[ind] <= target:
                rotarr = rotarr[ind:]
                stind += stind + ind
                continue
            else:
                rotarr = rotarr[:ind]
                continue
        if target == rotarr[0]:
            if stind < rotind:
                return stind + rotind
            else:
                return stind
        else:
            return -1


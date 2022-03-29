
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        divarr = nums
        stind = 0
        if len(divarr) == 1:
            if divarr[0] < target:
                return 1
            else:
                return 0
        while len(divarr) >1:
            isleft = False
            isright = False
            lenght = len(divarr)
            lefty = divarr[:(lenght // 2)]
            righty = divarr[(lenght // 2):]
            if righty[0] <= target:
                divarr = righty
                stind = stind + len(lefty)
                if righty[-1] < target:
                    isright = True
            else:
                divarr = lefty
                stind = stind
                if lefty[-1] < target:
                    isleft = True
                
        return stind + 1 if ((isleft) or (isright)) else stind              
        
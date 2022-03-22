
def indconv(num, numrows):
    if numrows ==1:
        period = 1
    else:
        period = numrows * 2 - 2
    numind = num
    q, r = divmod(numind, period)
    absr = min(r, period - r)
    return absr

class Solution:
    def convert(self, s:str, numRows:int) -> str:
        dic_zig = {}
        for ind in range(numRows):
            dic_zig[ind] = ''
        for ind, ss in enumerate(s):
            dic_zig[indconv(ind, numRows)] += ss

        ans = ''
        for val in dic_zig.values():
            ans += val
        return ans

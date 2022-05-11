def check(mid, position, m):
    m -= 1
    prev = position[0]
    for pos in position[1:]:
        if pos - prev >= mid:
            prev = pos
            m -= 1
    return True if m <=0 else False
    

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        ma = position[-1] - position[0]
        mi = 1
        ans = 1
        while ma>=mi:
            mid = (ma+mi) // 2
            if check(mid, position, m):
                ans = mid
                mi = mid + 1
            else:
                ma = mid - 1
        return ans
                
                
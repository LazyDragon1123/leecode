def factorial(n, m, divider=None):
    if divider is not None:
        res = 1 /divider
    else:
        res = 1
        
    for num in range(m, n +1):
        res *= num
        
    return res
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        divider = factorial(n-1,1)
        ans = factorial((n+m-2), m-1, divider= divider)
        return ans

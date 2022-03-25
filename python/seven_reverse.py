import re

limu = '2147483647'
limd = '2147483648'

class Solution:
    def reverse(self, x: int) -> int:
        xs = str(x)
        rev_xs = xs[::-1]
        if rev_xs[-1] == '-':
            rev_xs = rev_xs[:-1]
            if int(rev_xs[:-1]) < int(limd[:-1]):
                return -int(rev_xs)
            elif int(rev_xs[:-1]) == int(limd[:-1]):
                if int(rev_xs[-1]) <= int(limd[:-1]):
                    return -int(rev_xs)
                else:
                    return 0
            else:
                return 0
            
        else:
            if len(rev_xs) == 1:
                return int(rev_xs)
            if int(rev_xs[:-1]) < int(limu[:-1]):
                return int(rev_xs)
            elif int(rev_xs[:-1]) == int(limu[:-1]):
                if int(rev_xs[-1]) <= int(limu[:-1]):
                    return int(rev_xs)
                else:
                    return 0
            else:
                return 0
        
                
        
        
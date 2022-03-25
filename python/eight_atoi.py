limu = '2147483647'
limd = '2147483648'
digs = [str(i) for i in range(10)]

def rem_sp(inp):
    return inp.replace(' ', '')

def sign(inp):
    if len(inp) == 0:
        return 1, ''
    if '-' == inp[0]:
        return -1, inp[1:]
    elif '+' == inp[0]:
         return 1, inp[1:]
    else:
        return 1, inp

def ext_dig(inp):
    tmp = ''
    for char in inp:
        if char in digs:
            tmp+= char
        else:
            return tmp
    return tmp

def clamp(rev_xs, si):
    if len(rev_xs) == 0:
        return 0
    if si == -1:
        if int(rev_xs[:-1]) < int(limd[:-1]):
            return -int(rev_xs)
        elif int(rev_xs[:-1]) == int(limd[:-1]):
            if int(rev_xs[-1]) <= int(limd[:-1]):
                return -int(rev_xs)
            else:
                return -int(limd)
        else:
            return -int(limd)
        
    else:
        if len(rev_xs) == 1:
            return int(rev_xs)
        if int(rev_xs[:-1]) < int(limu[:-1]):
            return int(rev_xs)
        elif int(rev_xs[:-1]) == int(limu[:-1]):
            if int(rev_xs[-1]) <= int(limu[:-1]):
                return int(rev_xs)
            else:
                return int(limu)
        else:
            return int(limu)

class Solution:
    def myAtoi(self, s:str) -> int:
        s = rem_sp(s)
        
        si, s = sign(s)
        
        s = ext_dig(s)
        return clamp(s, si)


def ext_common(str1, str2):
    ret = ''
    for ind in range(min(len(str1),len(str2))):
        if str1[ind] == str2[ind]:
            ret += str1[ind]
        else:
            break
    return ret

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cand = strs[0]
        if len(strs) == 1:
            return cand
        else:
            for new in strs[1:]:
                cand = ext_common(cand, new)
        return cand

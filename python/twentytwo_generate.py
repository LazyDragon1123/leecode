from shutil import register_archive_format


def cand_generate(res, cand, on, cn, n):
    if on == n and cn ==n:
        res.append(cand)
        return
    if on < n:
        cand_generate(res, cand + '(', on + 1, cn, n)
    if cn < on:
        cand_generate(res, cand + ')', on, cn +1, n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion
        res = []
        cand_generate(res, cand, on, cn, n)
        return res
    
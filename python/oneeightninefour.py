class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idx = 0
        num = len(chalk)
        per_len = sum(chalk)
        k = k % per_len
        while True:
            if k - chalk[idx] < 0:
                return idx
            else:
                k -= chalk[idx]
                idx = (idx + 1) % num
        return idx
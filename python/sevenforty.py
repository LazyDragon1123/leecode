class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = {}
        sorted_uni_num = sorted(list(set(nums)))
        for i in nums:
            if dic.get(i) is None:
                dic[i] = i
            else:
                dic[i] += i
        prev = float('inf')
        dp_w = [0]
        dp_wo = [0]
        for i in sorted_uni_num:
            if abs(i - prev) == 1:
                dum = dp_w[-1]
                dp_w.append(max(dp_w[-1], dp_wo[-1] + dic[i]))
                dp_wo.append(max(dum, dp_wo[-1]))
                
            else:
                dum = dp_w[-1]
                dp_w.append(max(dp_w[-1] + dic[i], dp_wo[-1] + dic[i]))
                dp_wo.append(max(dum, dp_wo[-1]))
            prev = i
        return max(dp_w[-1], dp_wo[-1])
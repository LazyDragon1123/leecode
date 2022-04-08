class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1) == 0) or (len(nums2) == 0):
            return []
        dic = {}
        for i in nums1:
            if dic.get(i) is None:
                dic[i] = 1
            continue
        dic_int = {}
        for i in nums2:
            if dic.get(i) is not None:
                dic_int[i] = 1
            continue
        return list(dic_int.keys())

# # brute force approarch
# import numpy as np


# # brute force
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
#         # make posibble lists form two arrays
#         cands = []
#         sums = []
#         for i in nums1:
#             for j in nums2:
#                 sums.append(i+j)
#                 cands.append([i, j])
#         index_sorted = np.argsort(np.asarray(sums))
#         return cands_sorted[:k]
#         cands_sorted = np.asarray(cands)[index_sorted]
        
# # heapq
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         visited = set((0, 0))
#         h = [(nums1[0] + nums2[0], 0 , 0)]
#         ans = []
#         while(h and len(ans) < k):
#             s, i, j = heapq.heappop(h)
#             ans.append([i,j])
#             if 
#             heap.heappush(h, )
#             if i == j and i == 0:
#                 ans.append([nums1[i], num2[j]])
            
#             cand1 = [i+1,j]
#             cand2 = [i, j+1]
#             if cand1 >= cand2:
#                 ans.append(cand2)
#                 i+

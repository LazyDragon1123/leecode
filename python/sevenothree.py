import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums)[::-1][:k]
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        
    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            smallest = float('-inf')
        else:
            smallest = heapq.nsmallest(1, self.nums)[0]
        print(smallest)
        if val >= smallest:
            heapq.heappush(self.nums, val)
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
            return heapq.nsmallest(1, self.nums)[0]
        else:
            if not (len(self.nums) >= self.k):
                heapq.heappush(self.nums, val)
                return heapq.nsmallest(1, self.nums)[0]
            return smallest
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

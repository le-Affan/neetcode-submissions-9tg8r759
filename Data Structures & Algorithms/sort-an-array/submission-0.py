import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []

        for i in nums:
            heapq.heappush(heap, i)
        
        res = []

        for _ in range(len(nums)):
            element = heapq.heappop(heap)
            res.append(element)
        return res

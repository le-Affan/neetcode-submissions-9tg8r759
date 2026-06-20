class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, i * -1)
        
        while len(heap) > 1:
            s1 = -1 * (heapq.heappop(heap))
            s2 = -1 * (heapq.heappop(heap))

            if s1 > s2:
                heapq.heappush(heap, -1 * (s1 - s2))
        
        return -1 * heap[0] if heap else 0
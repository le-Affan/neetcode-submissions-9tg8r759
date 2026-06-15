import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, (-1 * i))
        
        while len(heap) > 1:
            stone1 = -1 * heapq.heappop(heap)
            stone2 = -1 * heapq.heappop(heap)

            if stone1 > stone2:
                newStone = -1 * (stone1 - stone2)
                heapq.heappush(heap, newStone)
            elif stone2 > stone1:
                newStone = -1 * (stone2 - stone1)
                heapq.heappush(heap, newStone)

        if len(heap) == 1:
            return -1 * heap[0]
        else:
            return 0



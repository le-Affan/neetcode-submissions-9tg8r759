import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def distance(list):
            return math.sqrt((list[0] * list[0] + list[1] * list[1]))

        for i in points:
            d = distance(i)

            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                smallest = heap[0]
                if d < distance(smallest):
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
        return heap
        
        

import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def distance(list):
            return math.sqrt((list[0] * list[0] + list[1] * list[1]))

        for i in points:
            d = -1 * distance(i)
            element = [d, i]
            
            if len(heap) < k:
                heapq.heappush(heap, element)
            else:
                smallest = heap[0]

                if d > smallest[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, element)
        return [item[1] for item in heap]
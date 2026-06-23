class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = [[-x, ch] for x, ch in [(a, 'a'), (b, 'b'), (c, 'c')] if x > 0]
        heapq.heapify(heap)
        q = deque()
        res = ""

        while heap:
            curr = heapq.heappop(heap)
            if len(res) >= 2 and curr[1] == res[-2] == res[-1]:
                q.append(curr)
                continue
            
            res += curr[1]
            curr[0] += 1

            if curr[0] != 0:
                heapq.heappush(heap, curr)

            if q:
                heapq.heappush(heap, q.popleft())
            
        
        return res




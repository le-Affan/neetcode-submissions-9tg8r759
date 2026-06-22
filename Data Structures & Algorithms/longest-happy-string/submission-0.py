class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-x, ch] for x, ch in [(a,'a'),(b,'b'),(c,'c')] if x > 0]
        heapq.heapify(heap)
        q = deque()
        res = ""

        while heap:
            
            curr = heapq.heappop(heap)

            if curr[0] <= -2:
                res += 2 * curr[1]
                curr[0] += 2
            else:
                res += curr[1]
                curr[0] += 1
            
            if q:
                heapq.heappush(heap, q.popleft())
            
            if curr[0] != 0:
                q.append(curr)
        return res
                
class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = Counter(s)

        for i in counts.values():
            if i > (len(s) + 1) // 2:
                return ""

        heap = [[-cnt, key] for key, cnt in counts.items()]

        heapq.heapify(heap)
        q = deque()
        res = ""

        while heap or q:
            curr = heapq.heappop(heap)
            res += curr[1]
            curr[0] += 1

            if q:
                heapq.heappush(heap, q.popleft())
                
            if curr[0] != 0:
                q.append(curr)

        return res



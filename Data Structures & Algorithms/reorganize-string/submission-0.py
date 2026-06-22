class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = Counter(s)
        heap = [[-cnt, key] for key, cnt in counts.items()]

        heapq.heapify(heap)
        q = deque()
        res = ""

        while heap or q:
            if not q and len(heap) == 1 and heap[0][0] < -1:
                return ""
            elif not heap and q[0][0] < -1:
                return ""
                
            if heap:
                curr = heapq.heappop(heap)
                res += curr[1]
                curr[0] += 1

                if curr[0] != 0:
                    q.append(curr)
            
            elif q:
                curr = q.popleft()
                res += curr[1]
                curr[0] += 1

                if curr[0] != 0:
                    heapq.heappush(heap, curr)
        
        return res



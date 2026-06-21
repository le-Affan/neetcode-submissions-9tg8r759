class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while q or heap:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time
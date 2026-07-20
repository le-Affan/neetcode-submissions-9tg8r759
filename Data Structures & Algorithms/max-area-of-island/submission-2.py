class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            curr = 1

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    R, C = row + dr, col + dc
                    if (R in range(rows) and
                        C in range(cols) and
                        grid[R][C] == 1 and
                        (R,C) not in visit):
                        visit.add((R,C))
                        q.append((R,C))
                        curr += 1
            return curr
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = max(res, bfs(r,c))
        return res

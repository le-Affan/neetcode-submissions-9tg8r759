class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def bfs(r,c,perimeter):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                perimeter += 4
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1
                    ):
                        perimeter -= 1
                        if (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
            return perimeter

        p = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    p = bfs(r,c,0)
        return p
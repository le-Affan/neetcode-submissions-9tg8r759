class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, cols = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]] # Right, Left, Up, Down in that order
                for dr, dc in directions:
                    r, c = row + dr, cols + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r,c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
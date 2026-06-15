class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(h), len(h[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(oceanSet,borderPoints):
            while borderPoints:
                r,c = borderPoints.popleft()
                oceanSet.add((r,c))
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (
                        row in range(ROWS) and
                        col in range(COLS) and
                        (row,col) not in oceanSet and
                        h[row][col] >= h[r][c]
                    ):
                        borderPoints.append((row,col))
                        oceanSet.add((row,col))

        pacific = set()
        l1 = collections.deque()

        for c in range(COLS):
            l1.append((0,c))
        for r in range(ROWS):
            l1.append((r,0))
        
        bfs(pacific,l1)

        
        atlantic = set()
        l2 = collections.deque()

        for c in range(COLS):
            l2.append((ROWS - 1, c))
        for r in range(ROWS):
            l2.append((r,COLS - 1))
        
        bfs(atlantic,l2)

        return list(atlantic & pacific)


        
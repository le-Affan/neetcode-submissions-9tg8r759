class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        q = collections.deque()
        safe = set()

        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0,c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1,c))
        
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r,0))
            if board[r][COLS - 1] == "O":
                q.append((r,COLS - 1))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            r,c = q.popleft()
            safe.add((r,c))
            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (
                    0 <= row < ROWS and
                    0 <= col < COLS and
                    board[row][col] == "O" and
                    (row,col) not in safe
                ):
                    q.append((row,col))
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in safe:
                    board[r][c] = "X"
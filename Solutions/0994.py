class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: #type: ignore
        
        rotten_oranges, tot_oranges = deque(), 0 #type: ignore
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def check():
            return len(visited) == tot_oranges


        for r in range(ROWS):
            for c in range(COLS):
                num = grid[r][c]
                if num == 1:
                    tot_oranges += 1
                elif num == 2:
                    visited.add((r, c))
                    tot_oranges += 1
                    rotten_oranges.append((r, c))
        res = 0
        if check(): return res
        

        while rotten_oranges:
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()
                delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in delta:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1 and (row, col) not in visited:
                        rotten_oranges.append((row, col))
                        visited.add((row, col))
            res += 1
            if check(): return res
        
        return -1
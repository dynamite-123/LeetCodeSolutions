class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: # type: ignore
        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            area = 1
            visited.add((i, j))
            q = collections.deque() # type: ignore
            q.append((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and 
                        grid[r][c] and (r, c) not in visited):
                        area += 1
                        visited.add((r, c))
                        q.append((r, c))
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j]:
                    max_area = max(bfs(i, j), max_area)
        return max_area
            
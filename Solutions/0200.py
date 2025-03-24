class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            q = collections.deque() # type: ignore
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:   
                    if row + dr in range(rows) and col + dc in range(cols) and grid[row + dr][col + dc] == '1' and (row + dr, col + dc) not in visited:
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    res += 1
        return res
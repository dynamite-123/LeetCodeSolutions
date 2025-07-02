from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        st = image[sr][sc]
        if st == color: return image

        ROWS = len(image)
        COLS = len(image[0])

        DIR = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        q = deque([(sr, sc)])
        visited = set()

        while q:
            i, j = q.popleft()
            image[i][j] = color

            for di, dj in DIR:
                ni, nj = i+di, j+dj
                if (
                    ni in range(ROWS) and
                    nj in range(COLS) and
                    (ni, nj) not in visited and
                    image[ni][nj] == st
                ):
                    
                    q.append((ni, nj))
                    visited.add((ni, nj))

        return image
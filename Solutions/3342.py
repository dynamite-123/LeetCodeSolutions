import heapq
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R, C = len(moveTime), len(moveTime[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        best = [[float('inf')] * C for _ in range(R)]

        h = []
        heapq.heappush(h, (0, 0, 0, 2))

        while h:
            time, x, y, prev = heapq.heappop(h)
            nt = 3 - prev
            for dx, dy in DIR:
                nx, ny = dx + x, dy + y
                if nx in range(R) and ny in range(C):
                    req = max(time + nt, moveTime[nx][ny] + nt)
                    if req < best[nx][ny]:
                        best[nx][ny] = req
                        heapq.heappush(h, (req, nx, ny, nt))
        

        return best[R - 1][C - 1]
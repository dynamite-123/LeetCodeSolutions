from typing import List
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        if N == 0:
            return [[0]]
        matrix = [[None for _ in range(2**N)] for _ in range(2**N)]
        
        def fill(n, rs, cs, start):
            if n == 2:
                matrix[rs][cs] = 3 + start
                matrix[rs][cs + 1] = 0 + start
                matrix[rs + 1][cs] = 2 + start
                matrix[rs + 1][cs + 1] = 1 + start

            else:
                t = n // 2
                fill(t, rs, cs + t, start)
                fill(t, rs + t, cs + t, start + t*t)
                fill(t, rs + t, cs, start + 2 * t*t)
                fill(t, rs, cs, start + 3 * t*t)
        
        fill(2**N, 0, 0, 0)
        return matrix
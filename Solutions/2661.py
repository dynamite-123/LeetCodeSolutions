class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int: # type: ignore
        m, n = len(mat), len(mat[0])
        h = {int: [int, int]}
        row, col = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                h[mat[i][j]] = [i, j]

        for ind in range(len(arr)):
            i, j = h[arr[ind]]
            row[i] += 1
            col[j] += 1

            if row[i] == n or col[j] == m:
                return ind
        return -1
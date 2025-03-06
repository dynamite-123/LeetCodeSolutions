class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:  # type: ignore
        res = []
        s = 0
        visited = set()
        for lnum in grid:
            for i in lnum:
                if i in visited:
                    res.append(i)
                    continue
                s += i
                visited.add(i)
        n = len(grid) ** 2
        res.append(n * (n + 1) // 2 - s)

        return res

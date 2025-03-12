class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int: # type: ignore
        res = l = 0
        n = len(colors)
        for r in range(1, n + 2):
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            if r - l + 1 == 3:
                res += 1
                l += 1
        return res

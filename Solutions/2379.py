class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        res = float('inf')
        while(r <= len(blocks)):
            count = blocks[l : r].count('W')
            res = min(res, count)
            r += 1
            l += 1
        return res
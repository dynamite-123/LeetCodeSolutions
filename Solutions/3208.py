class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: # type: ignore
        res = l = 0
        n = len(colors)

        for r in range(1, n + k - 1):
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            if r - l + 1 == k:
                res += 1
                l += 1
        return res

    # - Brute Force  
        # res, n = 0, len(colors)
        # l, r = 0, k - 1
        # while(r < n + k - 1):
        #     for i in range(l, r):
        #         if colors[i % n] == colors[(i + 1) % n]:
        #             break
        #         if i == r - 1:
        #             res += 1
        #     l += 1
        #     r += 1

        # return res
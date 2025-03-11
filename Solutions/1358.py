class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        l = 0
        hm = defaultdict(int) # type: ignore
        for r in range(len(s)):
            hm[s[r]] += 1
            while len(hm) >= 3:
                res += len(s) - r
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    hm.pop(s[l])
                l += 1
        return res
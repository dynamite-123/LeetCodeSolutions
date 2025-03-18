class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sc = list(set(s))
        def func(c):
            N, res, count = len(s), k, 0
            l= 0
            for r in range(N):
                if s[r] != c: count += 1
                if count > k:
                    while l < N and s[l] == c: 
                    
                        l += 1
                    count -= 1
                    l += 1
                res = max(res, r - l + 1)
            return res
        res = k
        for c in sc:
            res = max(res, func(c))
        return res
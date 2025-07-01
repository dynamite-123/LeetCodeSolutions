from typing import List
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        N = len(words)

        if N == 1 or N == 2: return [0] * N

        res = [None] * N
        precompute = [None] * (N - 1)
        f, b = [0] * N, [0] * N

        def prefix_len(s1, s2):
            l = 0
            for i, j in zip(s1, s2):
                if i != j:
                    break
                l += 1
            return l

        for i in range(N - 1):
            precompute[i] = prefix_len(words[i], words[i+1])
        mx1, mx2 = precompute[0] , precompute[-1]

        for i in range(N-1):
            mx1 = max(mx1, precompute[i])
            mx2 = max(mx2, precompute[N - i - 2])
            f[i+1] = mx1
            b[N-i-2] = mx2
        
        for i in range(N):
            if i == 0: res[i] = b[1]
            elif i == N-1: res[i] = f[N-2]
            else:
                res[i] = max(prefix_len(words[i-1], words[i+1]), f[i-1], b[i+1])
     
        return res
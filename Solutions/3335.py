from collections import Counter
from functools import cache
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # dynamic programming approach

        mod = 10**9 + 7
        counter = Counter(s)

        @cache
        def helper(c, k, res):
            if k < 26:
                if k < ord('z') - ord(c) + 1:
                    res += 1
                else:
                    res += 2
            elif c == 'z':
                res += helper('a', k - 26, 0)
                res += helper('b', k - 26, 0)
                res += helper('z', k - 26, 0)
            else:
                res += helper(c, k - 26, 0)
                res += helper(chr(ord(c) + 1), k - 26, 0)
            return res
        
        ans = 0
        for i, j in counter.items():
            ans += j * helper(i, t, 0)
            ans %= mod
        return ans % mod
            


        # simple array approach

        # mod = 10**9 + 7
        # freq = [0] * 26    
        # start = ord('a')
        # i = 25
        
        # for st in s:
        #     freq[ord(st) - start] += 1
        
        # for _ in range(t):
        #     freq[(i + 1) % 26] += freq[i]
        #     i -= 1
        #     if i == -1:
        #         i = 25

        # return sum(freq) % mod
from collections import defaultdict
from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for l in dominoes:
            l.sort()
        cache = defaultdict(int)

        for e1, e2 in dominoes:
            cache[(e1, e2)] += 1

        res = 0
        for n in cache.values():
            res += (n-1) * (n) // 2

        return res

from collections import Counter
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tmax, bmax = Counter(tops).most_common(1)[0][0], Counter(bottoms).most_common(1)[0][0]
        N = len(tops)
        res1 = res2 = 0

        for i in range(N):
            if tops[i] != tmax:
                if bottoms[i] == tmax:
                    res1 += 1
                else:
                    res1 = -1
                    break
        for i in range(N):
            if bottoms[i] != bmax:
                if tops[i] == bmax:
                    res2 += 1
                else:
                    res2 = -1
                    break
        
        return res1 if res1 < res2 and res1 != -1 else res2
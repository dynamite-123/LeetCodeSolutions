from typing import List
from math import ceil
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hm = Counter(answers)
        res = 0
        for val in hm:
            res += ceil(float(hm[val]) / (val+1)) * (val+1)
        
        return int(res)
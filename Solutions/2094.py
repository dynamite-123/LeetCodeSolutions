from typing import List
from collections import defaultdict
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1

        def good(x):
            temp = defaultdict(int)
            while x:
                d = x % 10
                x = x // 10
                temp[d] += 1
            for n, fq in temp.items():
                if fq > freq[n]:
                    return False
            return True
        
        res = []

        for i in range(100, 1000, 2):
            if good(i):
                res.append(i)

        return res
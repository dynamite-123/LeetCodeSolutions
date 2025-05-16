from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def helper(i, cnt, cur):
            if cnt == 0:
                if sum(cur) == n:
                    res.append(cur.copy())
                return
            
            for i in range(i, 10):
                helper(i + 1, cnt - 1, cur + [i])

        helper(1, k, [])
        
        return res
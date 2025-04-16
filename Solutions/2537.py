from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = defaultdict(int)
        count[nums[0]] += 1
        
        res = 0
        l = r = 0
        t = 0

        while(l <= r and r < N):
            if t >= k:
                res += N - r
                count[nums[l]] -= 1
                t = t - count[nums[l]]
                l += 1
            
            else:
                r += 1
                if r == N: break
                count[nums[r]] += 1
                t = t + count[nums[r]] - 1

        return res
from collections import defaultdict
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dn = len(set(nums))
        hm = defaultdict(int)

        l, r, N = 0, -1, len(nums)
        res = 0

        while (1):
            if len(hm) == dn:
                hm[nums[l]] -= 1
                if not hm[nums[l]]: hm.pop(nums[l])
                l += 1
                res += N - r
            else:
                r += 1
                if r == N: break
                hm[nums[r]] += 1
        
        return res
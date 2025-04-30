from collections import Counter
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N, res, count, l, max_num= len(nums), 0, 0, 0, max(nums)

        for r in range(N):
            if nums[r] == max_num:
                count += 1
            while count >= k:
                res += N - r
                if nums[l] == max_num:
                    count -= 1
                l += 1

        return res
from collections import defaultdict
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res, hm = 0, defaultdict(list)

        for i, n in enumerate(nums):
            if n in hm:
                for ind in hm[n]:
                    if not i * ind % k: res += 1
            hm[n].append(i)
        
        return res



        # Brute force

        # N = len(nums)
        # res = 0
        # for i in range(N - 1):
        #     for j in range(i+1, N):
        #         if not i*j % k and nums[i] == nums[j]:
        #             res += 1
        # return res
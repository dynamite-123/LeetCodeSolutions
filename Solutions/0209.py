from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # clean code
        N, l, s = len(nums), 0, 0
        res = []

        for r in range(N):
            s += nums[r]
            while s >= target:
                res.append(r - l + 1)
                s -= nums[l]
                l += 1
        return 0 if not res else min(res)
        

        # N = len(nums)
        # res = []
        # l, r = 0, -1
        # s = 0

        # while r < N:
        #     r += 1
        #     if r == N: break
        #     s += nums[r]
        #     while s >= target:
        #         res.append(r - l + 1)
        #         s -= nums[l]
        #         l += 1


        # if not res:
        #     return 0
        # return min(res)
            
        # brute force
        # N = len(nums)

        # res = []
        # for i in range(N):
        #     for j in range(i+1, N+1):
        #         if sum(nums[i: j]) >= target:
        #             res.append(len(nums[i: j]))

        # if not res:
        #     return 0
        
        # return min(res)
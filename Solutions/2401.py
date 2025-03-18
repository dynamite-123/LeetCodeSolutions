class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int: # type: ignore
        N = len(nums)
        temp = 0
        res = 0
        l = 0

        for r in range(N):
            while temp & nums[r]:
                temp ^= nums[l]
                l += 1
            temp |= nums[r]
            res = max(res, r - l + 1)
        return res

        # N = len(nums)
        # temp = 0
        # res = 0
        # l, r = 0, 0
        # while r < N and l < N:
        #     if not (temp & nums[r]):
        #         temp |= nums[r]
        #         r += 1
        #     else:
        #         temp ^= nums[l]
        #         l += 1
        #     res = max(res, r - l)
        # return res
            


class Solution:
    def canPartition(self, nums: List[int]) -> bool: #type: ignore
        S = sum(nums)
        if S & 1: return False
        cache = set()
        csum = 0
        for n in nums:
            for num in list(cache):
                cache.add(num + n)
            cache.add(n)
        return S // 2 in cache

        # BRUTE FORCE APPROACH: 0(2^n)
        # N, S = len(nums), sum(nums)

        # def helper(i, csum):
        #     if i == N:
        #         if csum == 0: return False
        #         return csum == S - csum

        #     return (
        #         helper(i + 1, csum) or 
        #         helper(i + 1, csum + nums[i])
        #     )

        # return helper(0, 0) 
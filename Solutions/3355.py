class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool: # type: ignore
        n = len(nums)
        dif = [0] * (n + 1)
        for l, r in queries:
            dif[l] += 1
            dif[r + 1] -= 1
        for i in range(1, n + 1):
            dif[i] += dif[i - 1]
        for i in range(n):
            if dif[i] < nums[i]:
                return False
        return True

        # - Brute Force

        # s = sum(nums)
        # for l, r in queries:
        #     for i in range(l, r + 1):
        #         if nums[i]:
        #             nums[i] -= 1 
        #             s -= 1

        # return s == 0
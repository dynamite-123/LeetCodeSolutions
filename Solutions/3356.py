class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int: # type: ignore
        n = len(nums)
        left, right = 0, len(queries)
        res = -1

        def good(target):
            dif = [0] * (n + 1)
            for l, r, val in queries[:target]:
                dif[l] += val
                dif[r + 1] -= val
            for i in range(1, n + 1):
                dif[i] += dif[i - 1]
            for i in range(n):
                if dif[i] < nums[i]:
                    return False
            return True
        
        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


        # - Brute Force

        # s = sum(nums)
        # res = 0
        # for l, r, val in queries:
        #     if not s: break
        #     for i in range(l, r + 1):
        #         sub = val if nums[i] >= val else nums[i]
        #         nums[i] -= sub
        #         s -= sub
        #     res += 1
        # if not s:
        #     return res
        # else:
        #     return -1

        
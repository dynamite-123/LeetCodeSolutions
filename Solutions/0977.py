class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: # type: ignore
        # single line solution
        # return sorted([i**2 for i in nums])
        N = len(nums)
        end = N - 1
        l, r = 0, N - 1
        res = [0] * N
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[end] = nums[r] ** 2
                r -= 1
            else:
                res[end] = nums[l] ** 2
                l += 1
            end -= 1
        return res
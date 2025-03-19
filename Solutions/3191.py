class Solution:
    def minOperations(self, nums: List[int]) -> int: #type: ignore
        res = 0
        for i in range(len(nums) - 2):
            if not nums[i]:
                res += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        return res if nums[-1] & nums[-2] else -1
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]: #type: ignore
        nums.sort()
        dp = {}

        for i, num in enumerate(nums):
            max_subset = []
            for j in range(i):
                if num % nums[j] == 0 and len(dp[nums[j]]) > len(max_subset):
                    max_subset = dp[nums[j]]
            dp[num] = max_subset + [num]

        return max(dp.values(), key=len)
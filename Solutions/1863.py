class Solution:
    def subsetXORSum(self, nums: List[int]) -> int: # type: ignore
        N = len(nums)

        def dfs(i, total):
            if i == N:
                return total
            return dfs(i + 1, total) + dfs(i + 1, total ^ nums[i])

        return dfs(0, 0)
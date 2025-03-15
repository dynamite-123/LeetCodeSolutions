class Solution:
    def rob(self, nums: List[int]) -> int: # type: ignore
        # - Optimal recursive

        N = len(nums)
        dp = {}
        def helper(ind):
            if ind > N - 1:
                return 0
            if ind in dp:
                return dp[ind]
            dp[ind] = max(nums[ind] + helper(ind + 2), nums[ind] + helper(ind + 3))

            return dp[ind]
        return max(helper(0), helper(1))


        # - Iterative approach

        # rob1 = rob2 = 0
        # for num in nums:
        #     curr = max(rob1 + num, rob2)
        #     rob1 = rob2
        #     rob2 = curr
        # return curr


        # - My Solution, idk why it sucks

        # N = len(nums)
        # dp = {}

        # def helper(s, ind):
        #     if ind > N - 1:
        #         return s

        #     if (s, ind) in dp:
        #         return dp[(s, ind)]
        #     dp[(s, ind)] = max(helper(s + nums[ind], ind + 2), helper(s + nums[ind], ind + 3))

        #     return dp[(s, ind)]
        # return max(helper(0, 0), helper(0, 1))
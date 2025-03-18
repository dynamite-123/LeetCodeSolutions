class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(x, res):
            if x >= n:
                res += 1
                return res
            if x in dp:
                return dp[x]
            dp[x] = helper(x + 1, res) + helper(x + 2, res)
            return dp[x]

        return helper(1, 0)
    
    # - caching using cache decorator

    # class Solution:
    # def climbStairs(self, n: int) -> int:
    #     @cache
    #     def helper(x, res):
    #         if x >= n:
    #             res += 1
    #             return res
    #         return helper(x + 1, res) + helper(x + 2, res)
    #     return helper(1, 0)
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int: #type: ignore
        nums = sorted([grid[i][j] for i in range(len(grid)) 
                        for j in range(len(grid[0]))])

        N, MOD = len(nums), nums[0] % x

        for num in nums:
            if num % x != MOD: return -1

        def ops(mid: int):
            res = 0
            dif = mid // x
            for num in nums:
                res += abs(dif - num // x)
            return res

        mid = nums[N // 2]

        return ops(mid)

        # nums = sorted([grid[i][j] for i in range(len(grid)) 
        #                 for j in range(len(grid[0]))])
        # res = 0
        # MOD = nums[0] % x
        # mid = nums[len(nums) // 2]
        # for num in nums:
        #     if num % x != MOD: return -1
        #     res += abs((mid // x - num // x))
        
        # return res
        
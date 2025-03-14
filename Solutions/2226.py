class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int: # type: ignore
        res = 0

        # - function to check if a given number of candies can be shared among k students or not
        def check(x: int) -> bool:
            if x == 0:
                return True
            res = 0
            for num in candies:
                res += num // x
            return res >= k

        # - binary search to find most number candies that can be shared
        start = 0
        end = max(candies)

        while start <= end:
            mid = (start + end) // 2
            if check(mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res
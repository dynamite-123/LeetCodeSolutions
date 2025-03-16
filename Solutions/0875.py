class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_valid(x):
            res = 0
            for num in piles:
                res += math.ceil(num / x)
            return res <= h

        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
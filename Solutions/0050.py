class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if not x:
                return 0
            if not n:
                return 1
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
        if n < 0:
            return 1 / helper(x, abs(n))
        return helper(x, n)
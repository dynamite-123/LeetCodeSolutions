class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if not x:
                return 0
            if not n:
                return 1
            res = helper(x, n // 2)
            print(res)
            res = res * res
            return x * res if n % 2 else res
        if n < 0:
            return 1 / helper(x, abs(n))
        return helper(x, n)

        # res = 1
        # p = abs(n)
        # while p > 0:
        #     if p & 1:
        #         res = res * x
        #     x *= x
        #     p >>= 1
        # if n < 0:
        #     return 1 / res
        # return res
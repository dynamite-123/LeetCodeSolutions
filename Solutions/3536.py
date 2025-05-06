class Solution:
    def maxProduct(self, n: int) -> int:
        e1 = e2 = -1

        while n:
            d = n % 10
            n = n // 10

            if d >= e1:
                e2 = e1
                e1 = d
            else:
                e2 = max(e2, d)

        return e1 * e2

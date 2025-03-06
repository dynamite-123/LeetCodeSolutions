class Solution:
    def superPow(self, a: int, b: List[int]) -> int: # type: ignore
        def pow(x, b) -> int:
            res = 1
            while b > 0:
                if b & 1:
                    res = res * x % 1337
                x = x * x % 1337
                b >>= 1
            return res
        res = 1
        for num in b:
            res = pow(res, 10) * pow(a, num) % 1337
        return res

    # doesn't work because b is a list
        # count = 0
        # def helper(rem):
        #     nonlocal count
        #     if count == b:
        #         return rem
        #     rem = rem % 1337 + a % 1337
        #     rem = rem % 1337
        #     count += 1
        #     helper(rem)

        # return helper(0)
